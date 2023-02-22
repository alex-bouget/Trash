import os

class Explorer(Plugins):
    def __init__(self) -> None:
        super().__init__(
            "explorer",
            "Explorer test",
            author="KromBlast",
            version="0.7.15"
        )
    
    def listdir(self, path: str) -> list:
        p = os.listdir(path)
        t = {}
        for i in p:
            t[i] = os.path.isdir(i)
        return t
    
    def getcwd(self) -> str:
        return os.getcwd()
    
    def move(self, path: str) -> None:
        os.chdir(path)

__kromblast__ = [Explorer]