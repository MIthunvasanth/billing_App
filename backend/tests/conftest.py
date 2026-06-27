import pytest


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--api-base-url",
        default="http://localhost:8000",
        help="Base URL for the running API server (used by E2E tests).",
    )


@pytest.fixture(scope="session")
def base_url(request: pytest.FixtureRequest) -> str:
    return request.config.getoption("--api-base-url")
