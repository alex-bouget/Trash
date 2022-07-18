import os
import runpy
from typing import Any, Dict
from .plugins import Plugins


class PluginLoader:
    plugins_path: str
    plugins: Dict[str, Plugins]

    def __init__(self, path: str):
        self.plugins_path = path
        self.plugins = {}
    
    def _load_plugin(self) -> None:
        for plugin in os.listdir(self.plugins_path):
            if plugin.endswith(".py"):
                self._load_plugin_data(plugin)

    def _load_plugin_data(self, plugin: str) -> None:
        temp = runpy.run_path(
            os.path.join(self.plugins_path, plugin),
            init_globals={"Plugins": Plugins}
        )
        for api_data in temp["__kromblast__"]:
            data = api_data()
            self.plugins[data.name] = data

    def get_plugins_data(self) -> Dict[str, list]:
        tree = {}
        for plugin in self.plugins:
            tree[plugin] = self.plugins[plugin].get_data()
        return tree

    def call_plugin_function(self, plugin: str, function_name: str, *args) -> Any:
        return self.plugins[plugin].call_function(function_name, *args)
