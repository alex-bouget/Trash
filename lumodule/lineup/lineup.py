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
        return self.int

    def descript(self, value):
        return self.type(value)


class String(EasyVar):
    def __init__(self, *args):
        super(String, self).__init__(str)
        self.value = " ".join(args)
        self.command = {
            "set": self.set,
            "get": self.get,
            "count": self.count,
            "linecut": self.linecut,
            "fresh": self.fresh
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


class Int(EasyVar):
    def __init__(self, *args):
        super(Int, self).__init__(int)
        self.value = int(args[0])


class Float(EasyVar):
    def __init__(self, *args):
        super(Float, self).__init__(float)
        self.value = float(args[0])


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
        return float(n1)+float(n2)

    def moins(self, n1, n2):
        return float(n1)-float(n2)

    def multi(self, n1, n2):
        return float(n1)*float(n2)

    def divide(self, n1, n2):
        return float(n1)/float(n2)

    def dividei(self, n1, n2):
        return float(n1)//float(n2)

    def exp(self, n1, n2):
        return float(n1)**float(n2)

    def modulo(self, n1, n2):
        return float(n1) % float(n2)


class Condition(Exec):
    def __init__(self):
        super(Condition, self).__init__()


class List(Exec):
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
        self.list = new.list

    def display(self):
        return "[" + ", ".join([str(i) for i in self.list]) + "]"
