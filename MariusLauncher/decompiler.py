from .Element import element


class Decompiler:
    def __init__(self):
        self.ui_width = 0
        self.ui_height = 0
        self.master_width = 0
        self.master_height = 0
        self.content_number = 0
        self.master = 0

    def load_element(self, master, json):
        aim = element[json["element"].lower()](master, json, self.content_number)
        if "content" in json.keys():
            for content_number in range(len(json["content"])):
                self.master_width, self.master_height = (aim.winfo_width(), aim.winfo_height())
                self.content_number = content_number
                self.load_element(aim, json["content"][content_number])

    def load_json(self, master, json):
        self.master = master
        self.ui_width, self.ui_height = (master.winfo_width(), master.winfo_height())
        for content_number in range(len(json)):
            self.master.update_idletasks()
            self.master_width, self.master_height = (master.winfo_width(), master.winfo_height())
            self.content_number = content_number
            self.load_element(master, json[content_number])
