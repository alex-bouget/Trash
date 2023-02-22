from .LoadingSystem import LoadingSys
from ....Lang import getlang


class BattleStartCanvas(LoadingSys):
    def __init__(self, master, lib):
        super().__init__(master)
        self.Lib = lib
        self.deck = []

    def start(self, battle_url_server, player_id, deck, battle_id):
        self.Lib.Server.StartBattle(battle_url_server, player_id, battle_id)
        self.deck = deck
        self.wr(getlang()["BattleStartCanvas"]["start"][0])
        self.after(500, self.loop1)

    def loop1(self):
        data = self.Lib.Server.BattleServer.Get()
        if data is None:
            self.after(500, self.loop1)
        elif data == "BattleServer.Server.Full":
            print("wut")
        elif data == "BattleServer.Server.Wait":
            self.Lib.Server.BattleServer.WaitServer()
            self.loop2()

    def loop2(self):
        data = self.Lib.Server.BattleServer.Get()
        if data is None:
            self.after(500, self.loop2)
        elif data in ["BattleServer.Server.Bdd_Problem", "BattleServer.Server.Client_Problem"]:
            print("wut")
        elif data == "BattleServer.Server.Wait_Player":
            self.Lib.Server.BattleServer.WaitServer()
            self.after(500, self.loop2)
        else:
            self.Starter = data.split(".")[-1]
            self.Lib.Server.BattleServer.SendDeck(self.deck)
            self.loop3()

    def loop3(self):
        data = self.Lib.Server.BattleServer.Get()
        if data is None:
            self.after(500, self.loop3)
        else:
            self.ret = data
            self.StartFinish = True
