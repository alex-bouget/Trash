from .thread import setup_thread_excepthook
from .hook import exception_hook
from .setup import setup
from .tklogger import setup as tk_setup
import sys
import logging
import logging.config


def log_setup(folder):
    logging.config.fileConfig("logging.conf")
    logging.root = setup(folder)
    logging.info("log initialized")
    pil_logger = logging.getLogger('PIL')
    pil_logger.setLevel(logging.INFO)
    sys.excepthook = exception_hook
    setup_thread_excepthook()
    tk_setup(folder)
