from .AuthServer import Auth_Server
from .BattleServer import Battle_Server
from .PrincipalServer import Principal_Server


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
    def __init__(self, url, player_id, battle_id):
        self.BattleSend, self.BattleGet = Battle_Server(url, player_id, battle_id)
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
        self.BattleSend([client_version, bdd_version])

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

    def StopServer(self):
        self.BattleSend("BattleServer.End")
        while self.Get() != "BattleServer.Task_Finish":
            pass
        del self.BattleSend, self.BattleGet


class PrincipalServerCom:
    def __init__(self, url, client_file):
        self.PrincipalSend, self.PrincipalGet = Principal_Server(url, client_file)
        self.PrincipalSend("PrincipalServer.Start")
        while True:
            ret = self.PrincipalGet()
            if ret is not None:
                break
        if ret != "PrincipalServer.begin":
            raise RuntimeError("Unspecified Problem: PrincipalServerCom.Start not return begin")

    def Get(self):
        return self.PrincipalGet()

    def CreateAccount(self, username, password):
        self.PrincipalSend("PrincipalServer.CreateAccount")
        self.PrincipalSend({"username": username, "password": password})

    def ConnectAccount(self, username, password):
        self.PrincipalSend("PrincipalServer.ConnectAccount")
        self.PrincipalSend({"username": username, "password": password})
