import os

class Loader:
    loader_path: str
    elioc_data: str

    def __init__(self, path: str) -> None:
        self.loader_path = path
        self.elioc_data = open(os.path.join(path, "elioc.file"), "r").read()
