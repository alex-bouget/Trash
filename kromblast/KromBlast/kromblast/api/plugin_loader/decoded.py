import os
import runpy
from typing import Dict
from .plugins import Plugins

class DecodedLoader:
    plugins: Dict[str, Plugins] = {}
    """All plugins loaded by kromblast."""

    def __init__(self) -> None:
        pass

    def load_plugin(self, path: str) -> None:
        """Load all plugins."""
        for plugin in os.listdir(path):
            if plugin.endswith(".py"):
                self._load_plugin_data(plugin, path)
        return self.plugins

    def _load_plugin_data(self, plugin: str, path: str) -> None:
        """Load a plugin."""
        temp = runpy.run_path(
            os.path.join(path, plugin),
            init_globals={"Plugins": Plugins}
        )
        for api_data in temp["__kromblast__"]:
            data = api_data()
            self.plugins[data.name] = data