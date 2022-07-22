from typing import Any
from ...exceptions import SubPluginException

"""
Plugins are used to extend the functionality of KromBlast.
It's a subclass for all plugins.
"""
class Plugins:
    name: str
    """Name of the plugins, used for identification in javascript."""
    description: str
    """Description of the plugin."""
    other_info: dict
    """Other informations of the plugins (author, version, github page, etc...)."""

    def __init__(self, name: str, description: str, **other_info) -> None:
        """Initialize the plugin."""
        self.name = name
        self.description = description
        self.other_info = other_info
    
    def __str__(self):
        """Return the name, description and information of the plugin."""
        return (self.name
            + "\n\n\n"
            + self.description 
            + "\n\n\n" 
            + "\n".join(key + " " + value for key, value in self.other_info.items())
        )
    
    def call_function(self, function: str, *args) -> Any:
        """Call a function of the plugin."""
        return getattr(self, function)(*args)

    def _sub_plugin(self, name: str) -> dict:
        """UNUSED. return the data of a subplugin."""
        if issubclass(getattr(self, name), Plugins):
            return getattr(self, name).get_data()
        else:
            return None
    
    def get_data(self) -> dict:
        """Return the data of the plugin for javascript implementation."""
        data_key = dir(self)
        for v in [
                    i
                    for i in data_key
                    if (i.startswith("__") and i.endswith("__"))
                    ]:
            del data_key[data_key.index(v)]
        def oopsi():
            """function for lock subplugins."""
            raise SubPluginException("Plugin can't have a subplugin")
        data = {
            i: (
                ["function"] if callable(getattr(self, i))
                else oopsi() if isinstance(getattr(self, i), Plugins) 
                else ["variable", getattr(self, i)]
            )
            for i in data_key
        }
        return data