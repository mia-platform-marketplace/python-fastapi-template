import platform
import os
import uvicorn
from fastapi import FastAPI

from src.logging import logger, StructuredMessage
from src.middleware import LoggingMiddleware
from src.api.probes import router as probes_router
from src.api.hello_world import router as hello_world_router

from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI(
    openapi_url="/documentation/json",
    docs_url=None,
    redoc_url=None
)

app.include_router(probes_router)
app.include_router(hello_world_router)

app.add_middleware(LoggingMiddleware, logger=logger)

http_port = int(os.environ.get('HTTP_PORT', 3000))

Instrumentator().instrument(app).expose(app, include_in_schema=False)


if __name__ == '__main__':
    logger.info(StructuredMessage(
        message="Starting service",
        python_version=platform.python_version(),
        http_port=http_port
    ))

    while True:
        uvicorn.run(
            app,
            host='0.0.0.0',
            port=http_port,
            log_config=None
        )
