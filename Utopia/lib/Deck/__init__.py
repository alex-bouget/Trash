"""
DeckLib
Library for Utopia
Created by MisterMine01

:class Deck:
"""
import json
import os
import time
import logging
from copy import deepcopy


class Deck:
    def __init__(self, deck_folder, server_name):
        self.deck_folder = deck_folder
        self.server_name = server_name
        self._deck = {}
        self.server_deck = {}
        self._start_deck()

    def _start_deck(self):
        if os.path.isfile(os.path.join(self.deck_folder, "deck.json")):
            self._deck = json.load(open(os.path.join(self.deck_folder, "deck.json")))
        else:
            self._deck = {"Time": time.time(), "Deck": {self.server_name: {}}}
        self.server_deck = self._deck["Deck"][self.server_name]
        self.save_deck()

    def save_deck(self):
        logging.info("Saving Deck")
        self._deck["Time"] = time.time()
        self._deck["Deck"][self.server_name] = self.server_deck
        open(os.path.join(self.deck_folder, "deck.json"), "w").write(json.dumps(self._deck))

    def add_deck(self, name, obj):
        if name not in self.server_deck.keys():
            self.server_deck[name] = deepcopy(obj)
            self.save_deck()

    def delete_deck(self, name):
        if name in self.server_deck.keys():
            del self.server_deck[name]
            self.save_deck()

    def get_deck_name(self): return self.server_deck.keys()

    def get_deck(self, name):
        if name in self.server_deck.keys():
            return self.server_deck[name]

    def change_deck(self, name, obj):
        if name in self.server_deck.keys():
            self.server_deck[name] = deepcopy(obj)
            self.save_deck()
