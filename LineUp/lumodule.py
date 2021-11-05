import os
import runpy
from .command import Exec

class LuModule:
    def __init__(self):
        self.class_data = {}

    def add_class(self, name, class_data):
        setattr(self, name, class_data)
        self.class_data[name] = getattr(self, name)


class ModuleSystem:
    def __init__(self):
        self.module_name = {}

    def add_modules(self, name):
        setattr(self, name, LuModule())
        self.module_name[name] = getattr(self, name)

    def add_class(self, module_name, class_name, class_data):
        self.module_name[module_name].add_class(class_name, class_data)


module = ModuleSystem()


def load_modules(module_folder):
    for folder in os.listdir(module_folder):
        module.add_modules(folder)
        for luc in os.listdir(os.path.join(module_folder, folder)):
            data = runpy.run_path(os.path.join(module_folder, folder, luc), init_globals={"Exec": Exec})
            module.add_class(folder, list(data.keys())[-1], list(data.values())[-1])


def decode_modules():
    data = {}
    for i in module.module_name.keys():
        for k, v in module.module_name[i].class_data.items():
            data[i+"-"+k] = v
    print(data)
    return data
