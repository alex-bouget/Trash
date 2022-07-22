from typing import Any, Dict
import webview
from .api import Api
from .exceptions import ModeError, InvalidWindowParameter

"""Window for kromblast (pywebview)."""
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
                raise ModeError(
                    "{}, invalid mode for api, must be server, local or hosted".format(
                        api_config["mode"]
                    )
                )
            self.api.mode = api_config["mode"]
        else:
            self.api.mode = "server"
        self.test_window(window_config)
        self.win = webview.create_window(
            title=api_config["title"],
            url=api_config["url"],
            js_api=self.api,
            **window_config
        )
        self.debug = api_config["debug"] if "debug" in api_config else False
        self.gui = "qt"

    def test_window(self, window: Dict[str, Any]) -> None:
        """Test the window configuration,
        raise Exception if a key is not valid."""
        all_key = [
            "width", "height", "x", "y", "resizable",
            "fullscreen", "min_size", "hidden",
            "frameless", "easy_drag", "minimized",
            "on_top", "confirm_close", "background_color",
            "transparent", "text_select", "localization"
        ]
        for key in window.keys():
            if key not in all_key:
                raise InvalidWindowParameter(
                    "{} is not a valid key for window".format(key))

    def show(self) -> None:
        """Show the window."""
        webview.start(
            gui=self.gui,
            debug=self.debug,
            http_server=(self.api.mode == "hosted")
        )
