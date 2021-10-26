from .CardLib import CardLib
from .ServerLib import ServerLib
from .Deck import Deck
from .Discord import DiscordLib
import os


class UtopiaLib:
    def __init__(self, principal_server_url, battle_server_url, folder, lang, version):
        self.folder = folder
        self.Server = ServerLib(principal_server_url, battle_server_url,
                                os.path.join(folder, "p.load", "account.json"),
                                os.path.join(folder, "s.load"),
                                version)
        self.Card = CardLib(os.path.join(folder, "s.load", self.Server.AuthServerName), lang)
        self.Deck = Deck(os.path.join(folder, "p.load"), self.Server.AuthServerName)
        self.Discord = DiscordLib()
