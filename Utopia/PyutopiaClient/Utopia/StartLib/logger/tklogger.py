import logging
import time
import os


def file_handler(folder):
    file = logging.getLogger("Tkinter_File")
    new_handler = logging.FileHandler(os.path.join(folder,
                                                   time.strftime("%Y.%m.%d-%H.%M.%S-Tkinter.log", time.localtime())))
    new_handler.formatter = file.handlers[0].formatter
    return new_handler


def setup(folder):
    tk = logging.getLogger("Tkinter")
    tk.addHandler(file_handler(folder))
    return tk
