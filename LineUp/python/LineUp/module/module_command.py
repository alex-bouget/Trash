from .lumodule import ModuleSystem
import os
import runpy
import json
from .command import Exec
from ..version import modules_version


module = ModuleSystem()


def load_modules(module_folder, file):
    for folder in json.load(open(file)):
        if os.path.isdir(os.path.join(module_folder, folder)):
            mod = json.load(open(os.path.join(module_folder, folder, "packages.json")))
            module_can = False
            for i in mod["packages-id"]["interpreter-version"]:
                if i in modules_version:
                    module_can = True
                    break
            if module_can:
                module.add_modules(mod["packages-name"])
                data = runpy.run_path(os.path.join(module_folder, folder, mod["py-files"]["file"]),
                                      init_globals={"Exec": Exec, "module": module})
                for class_name in mod["py-files"]["class-name"]:
                    module.add_class(mod["packages-name"], class_name, data[class_name])


def decode_modules():
    data = {}
    for i in module.module_name.keys():
        for k, v in module.module_name[i].class_data.items():
            data[i+"-"+k] = v
    return data
