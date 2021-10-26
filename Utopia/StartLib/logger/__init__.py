from .thread import setup_thread_excepthook
from .after import setup_after_excepthook
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
    if sys.argv[0].split(".")[-1] != "py":
        sys.excepthook = exception_hook
    setup_thread_excepthook()
    setup_after_excepthook()
    tk_setup(folder)
