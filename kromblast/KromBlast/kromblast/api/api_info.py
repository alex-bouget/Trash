from typing import List
from ..version import kromblast

"""Information for the api"""
class ApiInfo:
    is_debug: bool
    """kromblast is in debug mode"""
    krom_id: List[str]
    """all id accepted by kromblast"""

    def __init__(self, is_debug: bool, krom_id: List[str]) -> None:
        """Initialize the api info"""
        self.is_debug = is_debug
        self.krom_id = krom_id

    def is_kromblast_running(self) -> bool:
        """Test if the api is kromblast"""
        return True
    
    def is_debug_mode(self) -> bool:
        """Test if the api is in debug mode"""
        return self.is_debug
    
    def get_kromblast_version(self) -> dict:
        """Return the version of kromblast"""
        return kromblast
    
    def id_good(self, id_krom: str) -> bool:
        """Test if the id is good"""
        return self.krom_id.__contains__(id_krom)
    
    def log(self, *args):
        """Log a message in python print"""
        print(*args)