from typing import Any, Dict
import webview
from .api import Api
from KromBlast.kromblast import api

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
    api_mode: str
    """type of the code executed in the webview, (server, local, or hosted)"""

    def __init__(
        self,
        window_config: Dict[str, Any],
        api_config: Dict[str, Any],
    ) -> None:
        """Initialize the window."""
        self.api = Api(True, api_config["plugin_path"], api_config["krom_id"])
        if "mode" in api_config:
            if api_config["mode"] not in ["server", "local", "hosted"]:
                raise ValueError(
                    "api_config['mode'] must be 'server', 'local', or 'hosted'"
                )
            self.api.mode = api_config["mode"]
        else:
            self.api.mode = "server"
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
        webview.start(
            gui=self.gui,
            debug=self.debug,
            http_server=(self.api.mode == "hosted")
        )
