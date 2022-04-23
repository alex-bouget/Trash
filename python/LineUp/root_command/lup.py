from ..interpreter.line import Line

class Lup:
    def __init__(self, interpreter):
        self.interpreter = interpreter

    def load_command(self, file):
        return self.execute(file)
    
    def execute(self, file):
        for i in open(file).read().split(";"):
            data = Line(" ".join(i.split("\n"))).execute(self.interpreter.global_variable, self.interpreter.global_class)
            if isinstance(data, list) and data[0] == "/L_e*/":
                return data[1]
    
