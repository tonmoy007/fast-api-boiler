import os
from typing import Callable

import sentry_sdk
from fastapi import Depends, FastAPI, Request, Response
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.routing import APIRoute
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware








@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if os.getenv('DEPLOYMENT_ENV') != "dev":
    sentry_dsn = os.getenv('SENTRY_DSN')
    sentry_sdk.init(dsn=sentry_dsn)
    app = SentryAsgiMiddleware(app)

# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     deps=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )
