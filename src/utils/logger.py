import logging
import os
from ..config import LOG_DIR, LOG_FILE, LOG_LEVEL


def get_logger():
    """
    Initialize and return a logger.
    """
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    logger = logging.getLogger("chatbot_logger")
    if not logger.handlers:
        logger.setLevel(LOG_LEVEL)
        handler = logging.FileHandler(LOG_FILE)
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
