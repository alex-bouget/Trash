class Element:
    def load_calculation(self, string):
        if isinstance(string, str):
            for variable in [
                ["%ui_width%", self.root.winfo_width()],
                ["%ui_height%", self.root.winfo_height()],
                ["%master_width%", self.master.winfo_width()],
                ["%master_height%", self.master.winfo_height()],
                ["%content_number%", self.content_number]
            ]:
                string = str(variable[1]).join(string.split(variable[0]))
            try:
                return eval(string)
            except NameError:
                return string
        elif isinstance(string, int):
            return string

    def resize(self):
        for key in [
            ["configure", self.configure],
            ["place", self.place]
        ]:
            if key[0] in self.js.keys():
                params = {}
                for param in self.js[key[0]].keys():
                    params[param] = self.load_calculation(self.js[key[0]][param])
                key[1](**params)
        for child in self.winfo_children():
            try:
                child.resize()
            except AttributeError:
                pass