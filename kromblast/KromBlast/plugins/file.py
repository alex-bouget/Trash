import os

class FileApi(Plugins):
    def __init__(self) -> None:
        super().__init__(
            "File",
            "File system for kromblast",
            author="KromBlast",
            version="0.7.15"
        )
    
    def listdir(self, path: str) -> list:
        return os.listdir(path)
    
    def isfile(self, path):
        return os.path.isfile(path)
    
    def isdir(self, path):
        return os.path.isdir(path)
    
    def exists(self, path):
        return os.path.exists(path)
    
    def mkdir(self, path):
        return os.mkdir(path)
    
    def rmdir(self, path):
        return os.rmdir(path)
    
    def remove(self, path):
        return os.remove(path)
    
    def rename(self, old, new):
        return os.rename(old, new)
    
    def copy(self, old, new):
        return os.copy(old, new)
    
    def move(self, old, new):
        return os.move(old, new)
    
    def chdir(self, path):
        os.chdir(path)


__kromblast__ = [FileApi]    
