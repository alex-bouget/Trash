import os
import runpy
from typing import Dict, List
from .kbp import KBP
from .plugins import Plugins

class EncodedLoader:
    plugins: Dict[str, Plugins] = {}
    """All plugins loaded by kromblast."""
    krom_id: List[str]
    """List of krom_ids."""

    def __init__(self, krom_id: List[str]) -> None:
        """Initialize the encoded plugin loader."""
        self.krom_id = krom_id

    def load_plugin(self, path: str) -> Dict[str, Plugins]:
        """Load KromBlastPlugin (.kbp)."""
        if path.endswith(".kbp"):
            kbp = KBP(path, self.krom_id)
            for plugin in range(kbp.plugin_length()):
                self._load_plugin_data(kbp.plugin_to_path(plugin))
        return self.plugins

    def _load_plugin_data(self, plugin: str) -> None:
        """Load a plugin."""
        temp = runpy.run_path(
            os.path.join(plugin),
            init_globals={"Plugins": Plugins}
        )
        for api_data in temp["__kromblast__"]:
            data = api_data()
            self.plugins[data.name] = data