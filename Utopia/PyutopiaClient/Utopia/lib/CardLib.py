from .Card import CardSystem
import logging
from threading import Thread


class CardLib:
    def __init__(self, bdd_folder, lang):
        self.BddFolder = bdd_folder
        self.Model = {}
        self.ModelFinish = False
        self.Card = CardSystem(bdd_folder, lang)

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
            while len(self_lib.Model.keys()) != len(self_lib.Card.AllCard.CardData.keys()):
                pass
            self.ModelFinish = True
            logging.info("Model Loading Finish")

        for card_id in self.Card.AllCard.CardData.keys():
            Thread(target=lambda c=card_id: ModelSet(self, c)).start()  # creating all thread with card_id
        Thread(target=lambda: ModelFinish(self)).start()
