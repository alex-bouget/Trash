from typing import Dict, List
from .api_info import ApiInfo
from .plugins_loader import PluginLoader

"""Api injected in javascript"""
class Api(PluginLoader, ApiInfo):
    def __init__(self, is_debug: bool, plugins_path: str, krom_id: List[str]) -> None:
        """Initialize the api"""
        ApiInfo.__init__(self, is_debug, krom_id)
        PluginLoader.__init__(self, plugins_path)
    
    def get_plugins_data(self, krom_id: str) -> Dict[str, list]:
        """Return the data of all plugins if the id is good"""
        if not self.id_good(krom_id):
            return False
        self._load_plugin()
        return PluginLoader.get_plugins_data(self)