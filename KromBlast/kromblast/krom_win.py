from typing import Any, Dict
import webview
from .api import Api

"""
Window for kromblast (pywebview)."""
class Window:
    api: Api
    """Api injected in javascript"""
    win: webview.Window
    """Window of the window."""
    debug: bool
    """Debug mode."""
    gui: str
    """Gui used by the window."""

    def __init__(
        self,
        window_config: Dict[str, Any],
        api_config: Dict[str, Any],
    ) -> None:
        """Initialize the window."""
        self.api = Api(True, api_config["plugin_path"], api_config["krom_id"])
        self.win = webview.create_window(
            title=api_config["title"],
            url=api_config["url"],
            js_api=self.api,
            **window_config
        )
        if "debug" in api_config.keys():
            self.debug = api_config["debug"]
        else:
            self.debug = False
        self.gui = "gtk"

    def show(self) -> None:
        """Show the window."""
        webview.start(gui=self.gui, debug=self.debug)
