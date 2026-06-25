import hashlib

from fastapi import APIRouter, Depends, File, Form, HTTPException, Query, UploadFile

from app.api.dependencies.auth import get_current_user_id
from app.api.dependencies.container import get_container
from app.api.schema import SuccessResponse
from app.service.container import ServiceContainer

router = APIRouter()

_VALID_STATUSES = frozenset({"pending", "processing", "completed", "failed", "cancelled"})


@router.post("/", status_code=201)
async def create_job(
    file: UploadFile = File(...),
    bypass_cache: bool = Form(False),
    user_id: str = Depends(get_current_user_id),
    container: ServiceContainer = Depends(get_container),
) -> SuccessResponse:
    """Upload a PDF and create a new extraction job."""
    pdf_bytes = await file.read()
    # When bypass_cache=True pass content_hash=None so the service skips cache lookup.
    # TODO (M3): wire bypass_cache through to the cache check in JobService.create_job.
    content_hash = None if bypass_cache else hashlib.sha256(pdf_bytes).hexdigest()
    job = await container.job_service.create_job(
        user_id=user_id,
        pdf_filename=file.filename or "upload.pdf",
        pdf_bytes=pdf_bytes,
        content_hash=content_hash,
    )
    return SuccessResponse(message="Job created", data=job)


@router.get("/")
async def list_jobs(
    status: str | None = Query(None),
    user_id: str = Depends(get_current_user_id),
    container: ServiceContainer = Depends(get_container),
) -> SuccessResponse:
    """List the caller's jobs, optionally filtered by status."""
    if status is not None and status not in _VALID_STATUSES:
        raise HTTPException(
            status_code=422,
            detail=f"Invalid status '{status}'. Must be one of: {sorted(_VALID_STATUSES)}",
        )
    jobs = await container.job_service.list_jobs(user_id=user_id, status=status)
    return SuccessResponse(message="Jobs retrieved", data=jobs)


# NOTE: /active must be defined before /{job_id} so FastAPI matches the literal
# path before the parameterised one.
@router.get("/active")
async def get_active_jobs(
    user_id: str = Depends(get_current_user_id),
    container: ServiceContainer = Depends(get_container),
) -> SuccessResponse:
    """Return all jobs currently being processed. Never cached."""
    jobs = await container.job_service.get_active_jobs(user_id=user_id)
    return SuccessResponse(message="Active jobs retrieved", data=jobs)


@router.get("/{job_id}")
async def get_job(
    job_id: str,
    user_id: str = Depends(get_current_user_id),
    container: ServiceContainer = Depends(get_container),
) -> SuccessResponse:
    """Return full detail for a single job owned by the caller.

    A job owned by another user is indistinguishable from a non-existent job (404).
    """
    job = await container.job_service.get_job(user_id=user_id, job_id=job_id)
    return SuccessResponse(message="Job retrieved", data=job)


@router.delete("/{job_id}")
async def cancel_job(
    job_id: str,
    user_id: str = Depends(get_current_user_id),
    container: ServiceContainer = Depends(get_container),
) -> SuccessResponse:
    """Cancel a pending job. Returns 409 if already processing/completed/failed."""
    job = await container.job_service.cancel_job(user_id=user_id, job_id=job_id)
    return SuccessResponse(message="Job cancelled", data=job)
