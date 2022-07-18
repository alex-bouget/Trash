import os
import runpy
from typing import Any, Dict
from .plugins import Plugins

"""Loader for plugins."""
class PluginLoader:
    plugins_path: str
    """Path to the plugins dir."""
    plugins: Dict[str, Plugins]
    """All plugins loaded by kromblast."""

    def __init__(self, path: str):
        """Initialize the plugin loader."""
        self.plugins_path = path
        self.plugins = {}
    
    def _load_plugin(self) -> None:
        """Load all plugins."""
        for plugin in os.listdir(self.plugins_path):
            if plugin.endswith(".py"):
                self._load_plugin_data(plugin)

    def _load_plugin_data(self, plugin: str) -> None:
        """Load a plugin."""
        temp = runpy.run_path(
            os.path.join(self.plugins_path, plugin),
            init_globals={"Plugins": Plugins}
        )
        for api_data in temp["__kromblast__"]:
            data = api_data()
            self.plugins[data.name] = data

    def get_plugins_data(self) -> Dict[str, list]:
        """Return the data of all plugins."""
        tree = {}
        for plugin in self.plugins:
            tree[plugin] = self.plugins[plugin].get_data()
        return tree

    def call_plugin_function(self, plugin: str, function_name: str, *args) -> Any:
        """Call a function of a plugin."""
        return self.plugins[plugin].call_function(function_name, *args)
