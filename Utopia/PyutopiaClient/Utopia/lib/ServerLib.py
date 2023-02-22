from .Server import AuthServerCom, BattleServerCom, PrincipalServerCom
import json
import os


class ServerLib:
    def __init__(self, principal_server_url, battle_server_url, account_file, bdd_folder, version, client_path):
        self.BattleServerUrl = battle_server_url
        self.PrincipalServerUrl = principal_server_url
        self.Version = version
        self.BddFolder = bdd_folder
        self.PrincipalServer = PrincipalServerCom(self.PrincipalServerUrl, account_file, client_path)
        self.AuthServer = AuthServerCom(self.BattleServerUrl, bdd_folder)  # communication with AuthServer
        self.AuthServerName = self.AuthServer.GetServerName()  # Name of server
        self.AuthServer.LoadBdd()

    def StartBattle(self, url, player_id, battle_id):
        try:
            self.BattleServer.StopServer()
        except AttributeError:
            pass
        self.BattleServer = BattleServerCom(url, player_id, battle_id)
        self.BattleServer.Start(self.Version,
                                json.load(open(os.path.join(self.BddFolder, self.AuthServerName, "v.json")))[0])
