from ..System.LoadingSystem import LoadingSys


class StartCanvas(LoadingSys):
    def __init__(self, master, lib):
        super().__init__(master)
        self.Lib = lib
        self.loop1()
        # self.master.play_video("Ressources/Utopia/Video/loading.mp4")

    def loop2(self):
        if self.Lib.ModelFinish:
            self.StartFinish = True
        else:
            self.after(500, self.loop2)

    def loop1(self):
        data = self.Lib.AuthServer.Get()
        if data is None:
            self.after(500, self.loop1)
        elif data == "AuthServer.TestBddFinish":
            self.Lib.CreateModelInThread()
            self.wr.set("loading Model")
            self.loop2()
        else:
            self.wr.set(data)
            self.after(500, self.loop1)
