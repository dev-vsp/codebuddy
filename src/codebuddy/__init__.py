
import logging

from .console import cli
from .modules import config


__all__ = [
    'cli'
]

# Configuring logging
handlers = [
    logging.StreamHandler()
]

log_file = config.LOGGER.get("log_file")
if log_file:
    handlers.append(
        logging.FileHandler(log_file)
    )

logging.basicConfig(
    level=config.LOGGER.get("level"),
    format=config.LOGGER.get("format"),
    handlers=handlers
)
