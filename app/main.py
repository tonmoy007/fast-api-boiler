import os
from typing import Callable

import sentry_sdk
from fastapi import Depends, FastAPI, Request, Response
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.routing import APIRoute
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from starlette.middleware.cors import CORSMiddleware

from .deps import get_query_token
from .routers import items, users


class ValidationErrorLoggingRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            try:
                return await original_route_handler(request)
            except RequestValidationError as exc:
                body = await request.body()
                detail = {"errors": exc.errors(), "body": body.decode()}
                raise HTTPException(status_code=422, detail=detail)

        return custom_route_handler


if os.getenv('DEPLOYMENT_ENV') != "dev":
    sentry_dsn = os.getenv('SENTRY_DSN')
    sentry_sdk.init(dsn=sentry_dsn)
    app = FastAPI(dependencies=[Depends(get_query_token)])
    app = SentryAsgiMiddleware(app)
else:
    app = FastAPI(dependencies=[Depends(get_query_token)])

app.router.route_class = ValidationErrorLoggingRoute

app.include_router(users.router)
app.include_router(items.router)
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8099",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     deps=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
