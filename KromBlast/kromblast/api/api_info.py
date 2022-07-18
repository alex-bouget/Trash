from typing import List
from ..version import kromblast

class ApiInfo:
    is_debug: bool
    krom_id: list

    def __init__(self, is_debug: bool, krom_id: List[str]) -> None:
        self.is_debug = is_debug
        self.krom_id = krom_id

    def is_kromblast_running(self) -> bool:
        return True
    
    def is_debug_mode(self) -> bool:
        return self.is_debug
    
    def get_kromblast_version(self) -> dict:
        return kromblast
    
    def id_good(self, id_krom: str) -> bool:
        return self.krom_id.__contains__(id_krom)
    
    def log(self, *args):
        print(*args)