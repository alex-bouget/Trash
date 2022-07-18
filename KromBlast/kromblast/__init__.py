import json
from typing import Any, Dict
from .krom_win import Window
import configparser
import os


class Kromblast:
    window: Window
    config: Dict[str, Dict[str, Any]]

    def __init__(
        self,
        main_path: str,
        config_file: str,
        config_data: dict or None = None
    ) -> None:
        self.config = self._parse_config(config_file)
        self.config["Api"]["plugin_path"] = os.path.join(
            main_path, self.config["Api"]["plugin_path"])
        self.window = Window(
            self.config["Windows"],
            self.config["Api"]
        )

    def _parse_config(self, config_file: str) -> Dict[str, Dict[str, Any]]:
        config = configparser.ConfigParser()
        config.read(config_file)
        data = {}
        for section in config.sections():
            data[section] = {}
            for key, value in config[section].items():
                data[section][key] = json.loads(value)
        return data

    def show(self) -> None:
        self.window.show()
