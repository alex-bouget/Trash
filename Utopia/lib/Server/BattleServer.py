from .ServerParent import Server
import json


class BattleServ(Server):
    def __init__(self, url, player_id):
        super().__init__(url)
        self.PlayerId = player_id

    def Start(self, client_version, bdd_version):
        data = self.getJsBySystem("Start", {"PlayerId": self.PlayerId, "ClientVersion": client_version,
                                            "BddVersion": bdd_version})
        if data["System"] == "Party Full":
            self.thread_return.append("BattleServer.Server.Full")
        else:
            self.thread_return.append("BattleServer.Server.Wait")

    def Wait(self):
        data = self.getJsBySystem("WaitPlayer", {"PlayerId": self.PlayerId})
        if "Error" in data.keys():
            if data["Error"] == "Wait":
                self.thread_return.append("BattleServer.Server.Wait_Player")
            elif data["Error"] == "BddVersion":
                self.thread_return.append("BattleServer.Server.Bdd_Problem")
            elif data["Error"] == "ClientVersion":
                self.thread_return.append("BattleServer.Server.Client_Problem")
            else:
                raise RuntimeError("This Error doesn't exist\nplease check your client version")
        else:
            if data["Turn"] == "Begin":
                self.thread_return.append("BattleServer.Server.Player_Begin")
            elif data["Turn"] == "Waiting":
                self.thread_return.append("BattleServer.Server.Player_Waiting")
            else:
                raise RuntimeError("This key doesn't exist\nplease check your client version")

    def SendDeck(self, deck):
        data = self.getJsBySystem("SendDeck", {"PlayerId": self.PlayerId, "Deck": json.dumps(deck)})
        self.thread_return.append(data)

    def GetBattle(self):
        data = self.getJsBySystem("GetBattle", {"PlayerId": self.PlayerId})
        self.thread_return.append(data)

    def SendBattle(self, dat):
        if dat["CardId"] is None and dat["System"] is None:
            self.thread_return.append("BattleServer.Error.Card_and_System_None")
            return
        elif dat["CardId"] is None:
            self.getJsBySystem("SendBattle", {"PlayerId": self.PlayerId, "System": dat["System"]})
        elif dat["System"] is None:
            self.getJsBySystem("SendBattle", {"PlayerId": self.PlayerId, "CardId": dat["CardId"]})
        else:
            self.thread_return.append("BattleServer.Error.Card_and_System_Not_None")
            return
        # self.thread_return(data)

    def run(self):
        while self.GetSend() != "BattleServer.Start":
            pass
        self.thread_return.append("BattleServer.begin")
        while True:
            data = self.GetSend()
            if data == "BattleServer.End":
                self.thread_return.append("BattleServer.Task_Finish")
                break
            elif data == "BattleServer.StartConnection":
                param = self.GetSend().split(".")
                if param[0] != "BattleServer":
                    self.thread_return.append("BattleServer.Start.Error")
                else:
                    self.Start(param[1], param[2])
            elif data == "BattleServer.WaitServer":
                self.Wait()
            elif data == "BattleServer.Deck":
                self.SendDeck(self.GetSend())
            elif data == "BattleServer.GetBattle":
                self.GetBattle()
            elif data == "BattleServer.SendBattle":
                self.SendBattle(self.GetSend())


def Battle_Server(url, player_id):
    battle_class = BattleServ(url, player_id)
    battle_class.start()
    return battle_class.ThreadSend, battle_class.ThreadReturn
