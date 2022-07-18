from .api_info import ApiInfo
from .plugins_loader import PluginLoader

class Api(PluginLoader, ApiInfo):
    def __init__(self, is_debug: bool, plugins_path) -> None:
        ApiInfo.__init__(self, is_debug, ["null"])
        PluginLoader.__init__(self, plugins_path)