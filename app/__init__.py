import sentry_sdk
from fastapi import FastAPI, Depends
from fastapi_sqlalchemy import DBSessionMiddleware
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from starlette.middleware.cors import CORSMiddleware

from app.api.dependencies import content_type
from app.api.routers import include_api_routes
from app.core.config import TITLE, ALLOWED_HOSTS, SENTRY_DSN, DB
from app.middlewares.route_middlwares import ValidationErrorLoggingRoute


def create_app() -> FastAPI:
    app = FastAPI(title=TITLE, dependencies=[Depends(content_type.check)])
    app.router.route_class = ValidationErrorLoggingRoute

    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(DBSessionMiddleware, db_url=DB.to_string())
    app = include_api_routes(app)
    sentry_sdk.init(dsn=SENTRY_DSN)
    SentryAsgiMiddleware(app)
    return app
