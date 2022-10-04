import os
from abc import ABC, abstractmethod

class Decoder(ABC):
    code: str
    folder_constructor: str
    def __init__(self, code: str, folder_constructor: str) -> None:
        self.code = code
        self.folder_constructor = folder_constructor
    
    @abstractmethod
    def decode(self) -> str:
        """decode the code and return the header file"""
        pass