"""
CardLib
Library for Utopia
Created by MisterMine01
"""

from .CardData import AllCard
from .Image import Card_Model
import json
import os


class CardSystem:
    def __init__(self, bdd_folder, lang):
        """
        Card Library for Utopia with
        Card Lib and Image Card

        :param bdd_folder:
        :param lang:
        """
        self.BddFolder = bdd_folder
        self.Lang = lang
        while not os.path.isfile(os.path.join(bdd_folder, "data.json")):  # wait the loadBDD download the data
            pass
        self.data = json.load(open(os.path.join(bdd_folder, "data.json")))  # Load data
        self.AllCard = AllCard(self.data["Card"])  # Load Card Lib

    def ImageById(self, card_id):
        """
        Get Card 2D Model in Pillow Image

        :param card_id:
        :return:
        """
        return Card_Model(card_id, self.AllCard.getObj(card_id),
                          self.data["Rarity"][self.AllCard.getRarity(card_id)],
                          self.BddFolder, self.Lang)
