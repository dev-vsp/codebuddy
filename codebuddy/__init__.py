
import logging

from .console import cli
from .modules import LOGGER_CONFIG


__all__ = [
    'cli',
]

# Configuring logging
handlers = [
    logging.StreamHandler()
]

log_file = LOGGER_CONFIG.get("log_file")
if log_file:
    handlers.append(
        logging.FileHandler(log_file)
    )

logging.basicConfig(
    level=LOGGER_CONFIG.get("level"),
    format=LOGGER_CONFIG.get("format"),
    handlers=handlers
)
