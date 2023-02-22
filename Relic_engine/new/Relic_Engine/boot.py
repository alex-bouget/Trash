from .variables import Main, Camera


class Size:
    @staticmethod
    def change_width(value):
        Main.windows.configure(width=value)
        Main.relic_engine.configure(width=value)
        Main.x = value

    @staticmethod
    def change_height(value):
        Main.windows.configure(height=value)
        Main.relic_engine.configure(height=value)
        Main.y = value

    @staticmethod
    def resize(width=-1, height=-1):
        if width > 0:
            Size.change_width(value=width)
        if height > 0:
            Size.change_height(value=height)


class Binding:
    def __init__(self):
        self.data_binding = {}

    def bind(self, key, function):
        if key in self.data_binding.keys():
            raise KeyError("key bind already exist")
        Main.windows.bind(key, function)
        self.data_binding[key] = function
        print(self.data_binding)

    def unbind(self, key):
        if key not in self.data_binding.keys():
            raise KeyError("key bind not exist")
        Main.windows.unbind(key)
        del self.data_binding[key]

    def unbind_all(self):
        for key in self.data_binding.keys():
            Main.windows.unbind(key)

    def rebind_all(self):
        for key in self.data_binding.keys():
            Main.windows.bind(key, self.data_binding[key])


def on_boot():
    setattr(Main.relic_engine, "change_width", Size.change_width)
    setattr(Main.relic_engine, "change_height", Size.change_height)
    setattr(Main.relic_engine, "resize", Size.resize)
    bind = Binding()
    setattr(Main.relic_engine, "bind", bind.bind)
    setattr(Main.relic_engine, "unbind", bind.unbind)
    setattr(Main.relic_engine, "rebind_all", bind.rebind_all)
    setattr(Main.relic_engine, "unbind_all", bind.unbind_all)
    Main.relic_engine.reload_function["RelicCore-Camera"] = Camera.reload_camera
