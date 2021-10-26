from .Server import AuthServerCom, BattleServerCom, PrincipalServerCom
import json
import os


class ServerLib:
    def __init__(self, principal_server_url, battle_server_url, account_file, bdd_folder, version):
        self.BattleServerUrl = battle_server_url
        self.PrincipalServerUrl = principal_server_url
        self.Version = version
        self.BddFolder = bdd_folder
        self.PrincipalServer = PrincipalServerCom(self.PrincipalServerUrl, account_file)
        self.AuthServer = AuthServerCom(self.BattleServerUrl, bdd_folder)  # communication with AuthServer
        self.AuthServerName = self.AuthServer.GetServerName()  # Name of server
        self.AuthServer.LoadBdd()

    def StartBattle(self, url, player_id):
        """
        Start Server Battle

        :param url:
        :param player_id:
        :return:
        """
        self.BattleServer = BattleServerCom(url, player_id)
        self.BattleServer.Start(self.Version,
                                json.load(open(os.path.join(self.BddFolder, self.AuthServerName, "v.json")))[0])
