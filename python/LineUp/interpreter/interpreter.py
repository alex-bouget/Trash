from .line import Line
from ..root_command import Variable, Exit


class Interpreter:
    def __init__(self, module, e_type):
        self.global_variable = {
            "v": Variable(self),
            "e": Exit(self, e_type)
        }
        self.global_class = module

    def set_class(self, name, value):
        self.global_class[name] = value

    def execute(self, file):
        for i in open(file).read().split(";"):
            data = Line(" ".join(i.split("\n"))).execute(self.global_variable, self.global_class)
            if isinstance(data, list) and data[0] == "/L_e*/":
                return data[1]
