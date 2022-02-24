import micro_process
import json


class EpicExt:
    def __init__(self, lgnd):
        self.lgnd = lgnd
        self.logged = False
        temp = micro_process.MicroProcess([self.lgnd, "status", "--json"])
        t = temp.get_out()
        while t is None:
            t = temp.get_out()
        self.status = json.loads(t)
        if self.status["account"] != "<not logged in>":
            self.logged = True

    def auth(self):
        if self.logged:
            return
        temp = micro_process.MicroProcess([self.lgnd, "auth"])
        while not temp.is_stop():
            pass


if __name__ == "__main__":
    ext = EpicExt("legendary")
    while True:
        print(">>")
        t = input()
        if t == "auth":
            ext.auth()
        elif t == "exit":
            exit(0)