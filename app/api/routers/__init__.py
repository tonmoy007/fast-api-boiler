from fastapi import FastAPI

from . import users, accounts
from . import items


def include_api_routes(app: FastAPI) -> FastAPI:
    app.include_router(users.router)
    app.include_router(items.router)
    app.include_router(accounts.router)
    return app
