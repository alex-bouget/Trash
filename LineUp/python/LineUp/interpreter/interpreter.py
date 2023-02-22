from .line import Line
from ..root_command import Variable, Exit, Lup


class Interpreter:
    def __init__(self, module, e_type):
        self.global_variable = {
            "v": Variable(self),
            "e": Exit(self, e_type),
            "l": Lup(self)
        }
        self.global_class = module

    def set_class(self, name, value):
        self.global_class[name] = value

    def console(self):
        print("By MisterMine01\n\n")
        t = ""
        while True:
            while len(t) == 0 or t[-1] != ";":
                t = t+input(">>")
            t = " ".join(t.split(";"))
            t = " ".join(t.split("\n"))
            if "".join(t.split(" ")) == "exit":
                break
            elif "".join(t.split(" ")) == "loaded":
                print("class_loaded:")
                for i in self.global_class.keys():
                    print(i)
            elif "".join(t.split(" ")) == "var":
                for i in self.global_variable.keys():
                    print(i)
            else:
                try:
                    print(Line(t).execute(self.global_variable, self.global_class))
                except KeyError:
                    print("<<ERROR, command not found>>")
                except TypeError:
                    print("<<ERROR, command not use like it should>>")
            t = ""
