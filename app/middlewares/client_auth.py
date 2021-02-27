from starlette.types import ASGIApp


class ClientAuthMiddleware:
    def __init__(
            self,
            app: ASGIApp
    ) -> None:
        self.app=app

