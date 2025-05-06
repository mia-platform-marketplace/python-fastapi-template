import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from logging import Logger
from src.logging import logger, StructuredMessage

EXCLUDED_PATHS = ["/metrics", "/-/check-up", "/-/ready", "/-/healthz"]

class LoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, logger: Logger):
        super().__init__(app)
        self.logger = logger

    async def dispatch(self, request: Request, call_next):
        if request.url.path in EXCLUDED_PATHS:
            return await call_next(request)

        start_time = time.time()

        self.logger.debug(StructuredMessage(
            message="Incoming HTTP request",
            method=request.method,
            path=request.url.path,
        ))

        response = await call_next(request)

        process_time = round((time.time() - start_time) * 1000, 2)

        self.logger.info(StructuredMessage(
            message="HTTP response",
            method=request.method,
            path=request.url.path,
            status_code=response.status_code,
            duration_ms=process_time,
        ))

        return response
