"""
CardLib without Image
Library for Utopia
Created by MisterMine01
"""


class Card:
    def __init__(self, obj: dict):
        """
        Card Class with all characteristic

        :param obj:
        """
        self.obj = obj
        self.Att = obj["att"]
        self.Def = obj["def"]
        self.Price = obj["price"]
        self.Rarity = obj["rarity"]
        self.Name = obj["name"]
        self.Desc = obj["description"]


class AllCard:
    def __init__(self, obj: dict):
        """
        Card Class with all Card characteristics

        :param obj:
        """
        self.Card = {}
        for Id, Value in obj.items():
            self.Card[Id] = Card(Value)  # create Card characteristics one by one

    def getAtt(self, card_id):
        """
        :param card_id:
        :return:
        """
        return self.Card[card_id].Att

    def getDef(self, card_id):
        """
        :param card_id:
        :return:
        """
        return self.Card[card_id].Def

    def getPrice(self, card_id):
        """
        :param card_id:
        :return:
        """
        return self.Card[card_id].Price

    def getRarity(self, card_id):
        """
        :param card_id:
        :return:
        """
        return self.Card[card_id].Rarity

    def getName(self, card_id):
        """
        :param card_id:
        :return:
        """
        return self.Card[card_id].Name

    def getDesc(self, card_id):
        """
        :param card_id:
        :return:
        """
        return self.Card[card_id].Desc

    def getObj(self, card_id):
        """
        :param card_id:
        :return:
        """
        return self.Card[card_id].obj
