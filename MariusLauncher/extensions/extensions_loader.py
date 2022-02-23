import subprocess
import json


class Extension:
    def __init__(self, efs):
        self.efs = json.load(open(efs))

    def launch_process(self, params=None, *args):
        if params is None:
            params = []
        if isinstance(params, str):
            params = [params]
        params.extend(args)
        if isinstance(self.efs["extensions_executable"], str):
            self.efs["extensions_executable"] = [self.efs["extensions_executable"]]
        return subprocess.Popen([*self.efs["extensions_executable"], *params],
                                stdout=subprocess.PIPE,
                                stdin=subprocess.PIPE)
