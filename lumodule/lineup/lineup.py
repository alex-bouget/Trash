class EasyVar(Exec):
    def __init__(self, typer):
        super(EasyVar, self).__init__()
        self.type = typer
        self.value = None
        self.command = {
            "set": self.set,
            "get": self.get,
            "descript": self.descript
        }

    def set(self, p1):
        self.value = self.type(p1)

    def get(self):
        return self.value

    def descript(self, value):
        return self.type(value)


class StringL(EasyVar):
    def __init__(self, *args):
        super(String, self).__init__(str)
        self.value = " ".join(args)
        self.command = {
            "set": self.set,
            "get": self.get,
            "count": self.count,
            "linecut": self.linecut,
            "fresh": self.fresh,
            "descript": self.descript
        }

    def count(self, p1=None):
        if p1 is None:
            return len(self.string)
        else:
            return len(p1)

    def linecut(self, p1=None):
        return module.linup.List(*p1.split("\n"))

    def fresh(self, string, number):
        return module.lineup.List(*[string[i:i+int(number)] for i in range(0, len(string), int(number))])


class IntL(EasyVar):
    def __init__(self, args=0):
        super(Int, self).__init__(int)
        self.value = int(args)


class FloatL(EasyVar):
    def __init__(self, args=0):
        super(Float, self).__init__(float)
        self.value = float(args)


class Operation(Exec):
    def __init__(self):
        super(Operation, self).__init__()
        self.command = {
            "+": self.plus,
            "-": self.moins,
            "*": self.multi,
            "/": self.divide,
            "//": self.dividei,
            "**": self.exp,
            "%": self.modulo
        }

    def plus(self, n1, n2):
        return n1 + n2

    def moins(self, n1, n2):
        return n1 - n2

    def multi(self, n1, n2):
        return n1 * n2

    def divide(self, n1, n2):
        return n1 / n2

    def dividei(self, n1, n2):
        return n1 // n2

    def exp(self, n1, n2):
        return n1 ** n2

    def modulo(self, n1, n2):
        return n1 % n2


class Condition(Exec):
    def __init__(self):
        super(Condition, self).__init__()
        self.command = {
            "=": self.equal,
            ">=": self.much_equal,
            "<=": self.low_equal,
            "!=": self.not_equal
        }

    def equal(self, n1, n2):
        return n1 == n2

    def much_equal(self, n1, n2):
        return n1 >= n2

    def low_equal(self, n1, n2):
        return n1 <= n2

    def not_equal(self, n1, n2):
        return n1 != n2


class Process(Exec):
    def __init__(self, global_variable, global_class):
        super(Process, self).__init__()
        self.global_variable = global_variable
        self.global_class = global_class
        self.command = {
            "if": self.if_pro,
            "while": self.while_pro,
            "multiple": self.multiple
        }

    def if_pro(self, *args):
        # {} {} {}
        if args[0].execute(self.global_variable, self.global_class):
            return args[1].execute(self.global_variable, self.global_class)
        else:
            if len(args) == 3:
                return args[2].execute(self.global_variable, self.global_class)
        return None

    def multiple(self, *args):
        if isinstance(args[0], str):
            data = []
            for i in args[1].decoded_line:
                data.append(i[1].execute(self.global_variable, self.global_class))
            return data[int(args[0])]
        return [i[1].execute(self.global_variable, self.global_class) for i in args[0].decoded_line]

    def while_pro(self, *arg):
        print("no")


class ListL(Exec):
    def __init__(self, *args):
        super(List, self).__init__()
        self.list = [i for i in args]
        self.command = {
            "get": self.get,
            "set": self.set,
            "setnew": self.setnew,
            "display": self.display
        }

    def get(self, index, lister=None):
        if lister is None:
            return self.list[int(index)]
        else:
            return lister.get(index)

    def set(self, new):
        self.list.append(new)

    def setnew(self, new):
        if isinstance(new, list):
            self.list = new
        else:
            self.list = new.list

    def display(self):
        return "[" + ", ".join([str(i) for i in self.list]) + "]"
