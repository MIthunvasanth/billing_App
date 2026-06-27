"""E2E tests against a running API server (localhost:8000 by default).

Skipped automatically if the server is not reachable.
Run with:
    uv run --project backend pytest tests/test_job_lifecycle.py -v
Or against a different host:
    uv run --project backend pytest tests/test_job_lifecycle.py --api-base-url http://api:8000
"""
from __future__ import annotations

import uuid
from pathlib import Path

import httpx
import pytest

# ---------------------------------------------------------------------------
# Server availability guard — skip entire module if server not reachable
# ---------------------------------------------------------------------------

def _server_reachable(base_url: str) -> bool:
    try:
        r = httpx.get(f"{base_url}/health", timeout=3)
        return r.status_code == 200
    except Exception:
        return False


# Evaluated lazily inside the fixture so --base-url is respected
_SERVER_SKIP_REASON = "API server not running at configured base_url"


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

SAMPLE_PDF = Path(__file__).resolve().parents[2] / "data" / "doc_001.pdf"


@pytest.fixture(scope="module")
def client(base_url: str) -> httpx.Client:
    if not _server_reachable(base_url):
        pytest.skip(_SERVER_SKIP_REASON)
    with httpx.Client(base_url=base_url, timeout=30) as c:
        yield c


def _unique_email(prefix: str = "user") -> str:
    return f"{prefix}+{uuid.uuid4().hex[:8]}@test.invalid"


def _register_and_login(client: httpx.Client, email: str, password: str = "Test1234!") -> str:
    """Register a new user and return a Bearer token."""
    reg = client.post("/auth/register", json={"name": "Test User", "email": email, "password": password})
    assert reg.status_code in (200, 201), f"Register failed: {reg.status_code} {reg.text}"

    login = client.post("/auth/login", json={"email": email, "password": password})
    assert login.status_code == 200, f"Login failed: {login.status_code} {login.text}"
    data = login.json()
    token = data.get("token") or (data.get("user") or {}).get("token")
    assert token, f"No token in login response: {data}"
    return token


# ---------------------------------------------------------------------------
# Health check
# ---------------------------------------------------------------------------

class TestHealth:
    def test_health_ok(self, client: httpx.Client) -> None:
        r = client.get("/health")
        assert r.status_code == 200
        body = r.json()
        assert body.get("status") == "ok"
        assert body.get("db") == "ok"


# ---------------------------------------------------------------------------
# Auth
# ---------------------------------------------------------------------------

class TestAuth:
    def test_register_returns_token_or_user(self, client: httpx.Client) -> None:
        email = _unique_email("reg")
        r = client.post("/auth/register", json={"name": "Reg Test", "email": email, "password": "Test1234!"})
        assert r.status_code in (200, 201)
        body = r.json()
        assert "token" in body or "user" in body

    def test_login_returns_token(self, client: httpx.Client) -> None:
        email = _unique_email("login")
        client.post("/auth/register", json={"name": "Login Test", "email": email, "password": "Test1234!"})
        r = client.post("/auth/login", json={"email": email, "password": "Test1234!"})
        assert r.status_code == 200
        body = r.json()
        token = body.get("token") or (body.get("user") or {}).get("token")
        assert token


# ---------------------------------------------------------------------------
# Happy-path job lifecycle
# ---------------------------------------------------------------------------

class TestJobLifecycle:
    @pytest.fixture(autouse=True)
    def _setup(self, client: httpx.Client) -> None:
        self.client = client
        self.email_a = _unique_email("user_a")
        self.token_a = _register_and_login(client, self.email_a)
        self.auth_a = {"Authorization": f"Bearer {self.token_a}"}

    def test_post_job_creates_pending(self) -> None:
        assert SAMPLE_PDF.exists(), f"Sample PDF not found: {SAMPLE_PDF}"
        with SAMPLE_PDF.open("rb") as f:
            r = self.client.post("/jobs", files={"file": ("doc_001.pdf", f, "application/pdf")}, headers=self.auth_a)
        assert r.status_code == 201, f"Expected 201, got {r.status_code}: {r.text}"
        body = r.json()
        assert "job_id" in body or "id" in body
        assert body.get("status") == "pending"

    def test_list_jobs_contains_created_job(self) -> None:
        with SAMPLE_PDF.open("rb") as f:
            post_r = self.client.post("/jobs", files={"file": ("doc_001.pdf", f, "application/pdf")}, headers=self.auth_a)
        assert post_r.status_code == 201
        job_id = post_r.json().get("job_id") or post_r.json().get("id")

        list_r = self.client.get("/jobs", headers=self.auth_a)
        assert list_r.status_code == 200
        ids = [j.get("job_id") or j.get("id") for j in list_r.json()]
        assert job_id in ids

    def test_get_job_detail(self) -> None:
        with SAMPLE_PDF.open("rb") as f:
            post_r = self.client.post("/jobs", files={"file": ("doc_001.pdf", f, "application/pdf")}, headers=self.auth_a)
        job_id = post_r.json().get("job_id") or post_r.json().get("id")

        r = self.client.get(f"/jobs/{job_id}", headers=self.auth_a)
        assert r.status_code == 200
        body = r.json()
        assert (body.get("job_id") or body.get("id")) == job_id

    def test_cancel_pending_job_returns_200(self) -> None:
        with SAMPLE_PDF.open("rb") as f:
            post_r = self.client.post("/jobs", files={"file": ("doc_001.pdf", f, "application/pdf")}, headers=self.auth_a)
        job_id = post_r.json().get("job_id") or post_r.json().get("id")

        r = self.client.delete(f"/jobs/{job_id}", headers=self.auth_a)
        assert r.status_code == 200

        # Job should now be cancelled
        detail_r = self.client.get(f"/jobs/{job_id}", headers=self.auth_a)
        assert detail_r.status_code == 200
        assert detail_r.json().get("status") == "cancelled"


# ---------------------------------------------------------------------------
# Unhappy paths
# ---------------------------------------------------------------------------

class TestUnhappyPaths:
    @pytest.fixture(autouse=True)
    def _setup(self, client: httpx.Client) -> None:
        self.client = client
        self.email_a = _unique_email("ua")
        self.email_b = _unique_email("ub")
        self.token_a = _register_and_login(client, self.email_a)
        self.token_b = _register_and_login(client, self.email_b)
        self.auth_a = {"Authorization": f"Bearer {self.token_a}"}
        self.auth_b = {"Authorization": f"Bearer {self.token_b}"}

        # Upload a job as user_a
        assert SAMPLE_PDF.exists()
        with SAMPLE_PDF.open("rb") as f:
            r = client.post("/jobs", files={"file": ("doc_001.pdf", f, "application/pdf")}, headers=self.auth_a)
        assert r.status_code == 201
        self.job_id_a = r.json().get("job_id") or r.json().get("id")

    def test_get_nonexistent_job_returns_404(self) -> None:
        fake_id = str(uuid.uuid4())
        r = self.client.get(f"/jobs/{fake_id}", headers=self.auth_a)
        assert r.status_code == 404

    def test_delete_nonexistent_job_returns_404(self) -> None:
        fake_id = str(uuid.uuid4())
        r = self.client.delete(f"/jobs/{fake_id}", headers=self.auth_a)
        assert r.status_code == 404

    def test_isolation_user_b_cannot_see_user_a_job(self) -> None:
        """user_b fetching user_a's job must get 404 (not 403 — existence must not leak)."""
        r = self.client.get(f"/jobs/{self.job_id_a}", headers=self.auth_b)
        assert r.status_code == 404, (
            f"Expected 404 (existence must not leak to other users), got {r.status_code}"
        )

    def test_post_jobs_without_auth_rejected(self) -> None:
        with SAMPLE_PDF.open("rb") as f:
            r = self.client.post("/jobs", files={"file": ("doc_001.pdf", f, "application/pdf")})
        assert r.status_code in (401, 403)

    def test_post_jobs_with_invalid_token_rejected(self) -> None:
        with SAMPLE_PDF.open("rb") as f:
            r = self.client.post(
                "/jobs",
                files={"file": ("doc_001.pdf", f, "application/pdf")},
                headers={"Authorization": "Bearer invalid.token.here"},
            )
        assert r.status_code in (401, 403)

    def test_delete_job_when_cancelled_returns_409_or_404(self) -> None:
        """Double-cancel: first cancel succeeds (200), second must 409 or 404."""
        r1 = self.client.delete(f"/jobs/{self.job_id_a}", headers=self.auth_a)
        assert r1.status_code == 200

        r2 = self.client.delete(f"/jobs/{self.job_id_a}", headers=self.auth_a)
        assert r2.status_code in (409, 404)
