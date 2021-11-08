class String(Exec):
    def __init__(self):
        super(String, self).__init__()
        self.string = ""
        self.command = {
            "set": self.set,
            "get": self.get,
            "count": self.count,
            "linecut": self.linecut,
            "fresh": self.fresh
        }

    def set(self, p1):
        self.string = p1

    def get(self):
        return self.string

    def count(self, p1=None):
        if p1 is None:
            return len(self.string)
        else:
            return len(p1)

    def linecut(self, p1=None):
        return module.linup.List(*p1.split("\n"))

    def fresh(self, string, number):
        return module.lineup.List(*[string[i:i+int(number)] for i in range(0, len(string), int(number))])


class List(Exec):
    def __init__(self, *args):
        super(List, self).__init__()
        self.list = [i for i in args]
        self.command = {
            "get": self.get,
            "set": self.set
        }

    def get(self, index, list=None):
        if list is None:
            return self.list[int(index)]
        else:
            return list.get(index)

    def set(self, new):
        self.list.append(new)
