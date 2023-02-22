from .folders import SuperFolders
from .logger import log_setup
import os


def folder_setup(folder):
    file = SuperFolders()
    file.add_folder("Data", folder)
    file.add_folder("p.load", os.path.join(folder, "p.load"))
    file.add_folder("s.load", os.path.join(folder, "s.load"))
    file.add_folder("log", os.path.join(folder, "logs"))
    return file
