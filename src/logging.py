import os
import sys
import logging
import json

def _parse_log_level(log_level: str) -> int:
    log_level_value = logging.getLevelNamesMapping().get(log_level.upper())

    if log_level_value is None:
        raise ValueError(f"Invalid log level: {log_level}")
    
    return log_level_value

class StructuredMessage(object):
    def __init__(self, message, **kwargs):
        self.message = message
        self.kwargs = kwargs

    def __str__(self):
        log_data = {"message": self.message, **self.kwargs}
        return json.dumps(log_data)

enable_uvicorn_logging = os.environ.get('ENABLE_UVICORN_LOGGING', 'false') in ['true', '1', 'yes', 'y']
logging.getLogger("uvicorn").propagate = enable_uvicorn_logging

asyncio_log_level = _parse_log_level(os.environ.get('ASYNCIO_LOG_LEVEL', 'WARNING'))
logging.getLogger('asyncio').setLevel(asyncio_log_level)

application_log_level = _parse_log_level(os.environ.get('LOG_LEVEL', 'INFO'))
logging.basicConfig(
    stream=sys.stdout,
    level=application_log_level,
)

logger = logging.getLogger('application_logger')
