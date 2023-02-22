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
