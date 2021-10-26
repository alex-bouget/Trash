"""
UtopiaLib
Library for Utopia
Created by MisterMine01

:class UtopiaLib:
"""

from .Card import Card
from .Server import AuthServerCom, BattleServerCom
from .deck import Deck
import os
from threading import Thread
import json
import logging


class UtopiaLib:
    def __init__(self, server_url, folder, lang):
        """
        Library for Utopia

        :param server_url:
        :param folder:
        :param lang:
        """
        self.lang = lang
        self.ServerUrl = server_url
        self.folder = folder
        self.BddFolder = os.path.join(folder, "s.load")
        self.AuthServer = AuthServerCom(self.ServerUrl, self.BddFolder)  # communication with AuthServer
        self.AuthServerName = self.AuthServer.GetServerName()  # Name of server
        self.AuthServer.LoadBdd()  # Start Bdd
        self.Card = Card(os.path.join(self.BddFolder, self.AuthServerName), self.lang)
        self.Deck = Deck(os.path.join(folder, "p.load"), self.AuthServerName)
        self.Model = {}
        self.ModelFinish = False

    def CreateModelInThread(self):
        """
        Create Card 2D Model in Pillow Image

        :return:
        """

        def ModelSet(self_lib, model_id):
            """
            Create Pillow Image and save in UtopiaLib.Model dict
            with key: model_id

            :param self_lib:
            :param model_id:
            :return:
            """
            self_lib.Model[model_id] = self_lib.Card.ImageById(model_id)

        def ModelFinish(self_lib):
            """
            Waiting all Image for return ModelFinish

            :param self_lib:
            :return:
            """
            while len(self_lib.Model.keys()) != len(self_lib.Card.Card.Card.keys()):
                pass
            self.ModelFinish = True
            logging.info("Model Loading Finish")

        for card_id in self.Card.Card.Card.keys():
            Thread(target=lambda c=card_id: ModelSet(self, c)).start()  # creating all thread with card_id
        Thread(target=lambda: ModelFinish(self)).start()

    def StartBattle(self, url, player_id, version):
        """
        Start Server Battle

        :param url:
        :param player_id:
        :param version:
        :return:
        """
        self.BattleServer = BattleServerCom(url, player_id)
        self.BattleServer.Start(version,
                                json.load(open(os.path.join(self.BddFolder, self.AuthServerName, "v.json")))[0])
