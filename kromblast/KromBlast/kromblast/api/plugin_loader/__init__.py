import os
from typing import Any, Dict, List
from .plugins import Plugins
from .decoded import DecodedLoader
from .encoded import EncodedLoader

"""Loader for plugins."""
class PluginLoader:
    plugins_path: str
    """Path to the plugins dir."""
    plugins: Dict[str, Plugins]
    """All plugins loaded by kromblast."""
    plugin_type: str
    """type of the plugin (encoded, decoded)"""

    def __init__(self, path: str):
        """Initialize the plugin loader."""
        self.plugins_path = path
        self.plugin_type = "encoded" if os.path.isfile(self.plugins_path) else "decoded"
        self.plugins = {}
    
    def _load_plugin(self, krom_id: List[str]) -> None:
        """Load all plugins."""
        if len(self.plugins.keys()) != 0:
            return
        if self.plugin_type == "decoded":
            self.plugins = DecodedLoader().load_plugin(self.plugins_path)
        else:
            self.plugins = EncodedLoader(krom_id).load_plugin(self.plugins_path)

    def get_plugins_data(self) -> Dict[str, list]:
        """Return the data of all plugins."""
        tree = {}
        for plugin in self.plugins:
            tree[plugin] = self.plugins[plugin].get_data()
        return tree

    def call_plugin_function(self, plugin: str, function_name: str, *args) -> Any:
        """Call a function of a plugin."""
        return self.plugins[plugin].call_function(function_name, *args)
