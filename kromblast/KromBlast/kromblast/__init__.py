import json
from typing import Any, Dict
from .krom_win import Window
from .exceptions import ConfigJsonError
import configparser
import os

"""Kromblast class."""
class Kromblast:
    window: Window
    """Window of kromblast."""
    config: Dict[str, Dict[str, Any]]
    """The configuration of Kromblast."""

    def __init__(
        self,
        main_path: str,
        config_file: str
    ) -> None:
        """Initialize Kromblast."""
        self.config = self._parse_config(config_file)
        self.config["Api"]["plugin_path"] = os.path.join(
            main_path, self.config["Api"]["plugin_path"])
        self.window = Window(
            self.config["Windows"],
            self.config["Api"]
        )

    def _parse_config(self, config_file: str) -> Dict[str, Dict[str, Any]]:
        """Parse the config file."""
        config = configparser.ConfigParser()
        config.read(config_file)
        data = {}
        for section in config.sections():
            data[section] = {}
            for key, value in config[section].items():
                try:
                    data[section][key] = json.loads(value)
                except json.JSONDecodeError:
                    raise ConfigJsonError(
                        "Invalid json in config file for {}.{}".format(
                            section, key)
                    )
        return data

    def show(self) -> None:
        """Show the window."""
        self.window.show()
