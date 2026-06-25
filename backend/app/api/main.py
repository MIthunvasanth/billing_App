from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.routes import auth, health, jobs
from app.config.settings import get_settings
from app.core.common.logger import configure_json_logging
from app.core.context_manager import ContextManager
from app.service.container import ServiceContainer
from app.service.exceptions import BaseServiceException


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    configure_json_logging(settings.LOG_LEVEL, settings.ENVIRONMENT)

    # billing role — full access; used for auth queries (session/user/account tables)
    admin_cm = ContextManager(settings)
    await admin_cm.initialize()

    # billing_app role — subject to RLS; used for all job operations
    app_cm = ContextManager(
        settings,
        connection_string=settings.APP_DB_CONNECTION_STRING or settings.POSTGRES_CONNECTION_STRING,
    )
    await app_cm.initialize()

    app.state.admin_cm = admin_cm
    app.state.container = ServiceContainer(app_cm)

    yield

    await admin_cm.close()
    await app_cm.close()


app = FastAPI(title="Medical Billing Extraction API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(BaseServiceException)
async def service_exception_handler(request: Request, exc: BaseServiceException):
    return JSONResponse(
        status_code=exc.http_status.value,
        content=exc.to_dict(),
    )


app.include_router(health.router, tags=["Health"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])
