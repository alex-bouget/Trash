from typing import Any, Dict
import webview
from .api import Api


class Window:
    api: Api
    win: webview.Window
    debug: bool
    gui: str

    def __init__(
        self,
        window_config: Dict[str, Any],
        api_config: Dict[str, Any],
    ) -> None:
        self.api = Api(True, api_config["plugin_path"])
        self.win = webview.create_window(
            title=api_config["title"],
            url=api_config["url"],
            js_api=self.api,
            **window_config
        )
        self.debug = api_config["debug"] == "true"
        self.gui = "gtk"

    def show(self) -> None:
        webview.start(gui=self.gui, debug=self.debug)
