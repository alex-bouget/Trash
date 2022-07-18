from typing import Any


class Plugins:
    name: str
    description: str
    other_info: dict

    def __init__(self, name, description, **other_info) -> None:
        self.name = name
        self.description = description
        self.other_info = other_info
    
    def __str__(self):
        return (self.name
            + "\n\n\n"
            + self.description 
            + "\n\n\n" 
            + "\n".join(key + " " + value for key, value in self.other_info.items())
        )
    
    def call_function(self, function, *args) -> Any:
        return getattr(self, function)(*args)

    def _sub_plugin(self, name: str) -> dict:
        if issubclass(getattr(self, name), Plugins):
            return getattr(self, name).get_data()
        else:
            return None
    
    def get_data(self) -> dict:
        data_key = dir(self)
        for v in [
                    i
                    for i in data_key
                    if (i.startswith("__") and i.endswith("__"))
                    ]:
            del data_key[data_key.index(v)]
        def oopsi():
            raise Exception("Plugin can't have a subplugin")
        data = {
            i: (
                ["function"] if callable(getattr(self, i))
                else oopsi() if isinstance(getattr(self, i), Plugins) 
                else ["variable", getattr(self, i)]
            )
            for i in data_key
        }
        return data