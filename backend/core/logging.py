import logging
from loguru import logger
import sys

# Disable default uvicorn logs for cleaner output
logging.getLogger("uvicorn").handlers = []

logger.remove()
logger.add(sys.stderr, level="INFO", format="<green>{time}</green> | <level>{message}</level>")

def get_logger(name: str):
    """Get a configured logger instance."""
    return logger.bind(name=name)
