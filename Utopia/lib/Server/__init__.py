from .AuthServer import Auth_Server
from .BattleServer import Battle_Server


class AuthServerCom:
    def __init__(self, url, folders):
        self.AuthSend, self.AuthGet = Auth_Server(url, folders)
        self.AuthSend("AuthServer.Start")
        while True:
            ret = self.AuthGet()
            if ret is not None:
                break
        if ret != "AuthServer.begin":
            raise RuntimeError("Unspecified Problem: AuthServerCom.Start not return begin")

    def Get(self):
        return self.AuthGet()

    def LoadBdd(self):
        self.AuthSend("AuthServer.TestBdd")

    def GetServerName(self):
        self.AuthSend("AuthServer.ServerName")
        while True:
            ret = self.AuthGet()
            if ret is not None:
                break
        name = ret.split(".")
        del name[0]
        del name[0]
        return ".".join(name)


class BattleServerCom:
    def __init__(self, url, player_id):
        self.BattleSend, self.BattleGet = Battle_Server(url, player_id)
        self.BattleSend("BattleServer.Start")
        while True:
            ret = self.BattleGet()
            if ret is not None:
                break
        if ret != "BattleServer.begin":
            raise RuntimeError("Unspecified Problem: BattleServerCom.Start not return begin")

    def Get(self):
        return self.BattleGet()

    def Start(self, client_version, bdd_version):
        self.BattleSend("BattleServer.StartConnection")
        self.BattleSend("BattleServer." + client_version + "." + bdd_version)

    def WaitServer(self):
        self.BattleSend("BattleServer.WaitServer")

    def SendDeck(self, deck):
        self.BattleSend("BattleServer.Deck")
        self.BattleSend(deck)

    def GetBattle(self):
        self.BattleSend("BattleServer.GetBattle")

    def SendBattle(self, card_id=None, system=None):
        self.BattleSend("BattleServer.SendBattle")
        self.BattleSend({"CardId": card_id, "System": system})
