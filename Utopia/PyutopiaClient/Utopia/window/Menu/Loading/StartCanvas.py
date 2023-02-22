from .LoadingSystem import LoadingSys
from ....Lang import getlang


class StartCanvas(LoadingSys):
    def __init__(self, master, lib):
        super().__init__(master)
        self.Lib = lib

    def loop2(self):
        if self.Lib.Card.ModelFinish:
            self.StartFinish = True
        else:
            self.after(500, self.loop2)

    def start(self):
        data = self.Lib.Server.AuthServer.Get()
        if data is None:
            self.after(500, self.start)
        elif data == "AuthServer.TestBddFinish":
            self.Lib.Card.CreateModelInThread()
            self.wr(getlang()["StartCanvas"]["start"][0])
            self.loop2()
        else:
            self.wr(data)
            self.after(500, self.start)
