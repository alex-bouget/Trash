import logging
import logging.config
import time
import os


def log_setup(folder):
    logging.config.fileConfig("logging.conf")
    console = logging.getLogger("Console")
    file = logging.getLogger("File")
    new_handler = logging.FileHandler(os.path.join(folder, time.strftime("%Y.%m.%d-%H.%M.%S.log", time.localtime())))
    new_handler.formatter = file.handlers[0].formatter
    console.addHandler(new_handler)
    logging.root = console
    logging.info("log initialized")
