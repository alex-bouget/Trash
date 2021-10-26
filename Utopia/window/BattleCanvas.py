from .Battle import GameCanvas
from .System.DeckChoiceSystem import DeckChoiceSys
from .Loading.BattleStartCanvas import BattleStartCanvas
import os
import logging
import json


class Battle:
    def __init__(self, master, player_id, lib, game_version):
        self.game_canvas = GameCanvas(master, player_id,
                                      os.path.join(lib.BddFolder, lib.AuthServerName, "font.ttf"),
                                      lib.Model, lib.Card.Card,
                                      {"Hand": self.Hand, "Board": self.Board, "Enemy": self.Enemy, "Pass": self.Pass})
        self.start_canvas = BattleStartCanvas(master, lib)
        self.Deck = DeckChoiceSys(master, "grey", lib.Deck.get_deck_name(), {"set": self.choice_deck})
        self.player_id = player_id
        self.lib = lib
        self.game_version = game_version
        self.dico = {}
        self.battle_server = ""

    def startBattle(self, deck, battle_server):
        self.start_canvas.place(x=0, y=0)
        self.start_canvas.start(battle_server, self.player_id, self.game_version, deck)
        self.looping1()

    def starting(self, battle_server):
        self.battle_server = battle_server
        self.Deck.place(x=0, y=0)

    def choice_deck(self, name):
        self.Deck.place_forget()
        self.startBattle(self.lib.Deck.get_deck(name), self.battle_server)

    def looping1(self):
        if self.start_canvas.StartFinish:
            self.start_canvas.place_forget()
            self.game_canvas.place(x=0, y=0)
            self.dico = self.start_canvas.ret
            self.game_canvas.change_battle(self.dico)
            self.lib.BattleServer.GetBattle()
            self.looping2()
        else:
            self.start_canvas.after(500, self.looping1)

    def looping2(self):
        data = self.lib.BattleServer.Get()
        if data is None:
            self.game_canvas.after(500, self.looping2)
        else:
            if self.dico != data:
                logging.debug("BattleSys: " + json.dumps(data))
                self.dico = data
                self.game_canvas.change_battle(data)
            self.lib.BattleServer.GetBattle()
            self.game_canvas.after(500, self.looping2)

    def Hand(self, value):
        if self.dico["Phase"]["Phase"] == "Main" and self.dico["Phase"]["PlayerId"] == self.player_id:
            self.lib.BattleServer.SendBattle(card_id=value)

    def Board(self, value):
        if (self.dico["Phase"]["Phase"] == "Battle" and self.dico["Phase"]["PlayerId"] == self.player_id) or (
                self.dico["Phase"]["Phase"] == "Def" and self.dico["Phase"]["PlayerId"] != self.player_id):
            self.lib.BattleServer.SendBattle(card_id=value)

    def Enemy(self, value):
        if self.dico["Phase"]["Phase"] == "Destroy" and self.dico["Phase"]["PlayerId"] == self.player_id:
            self.lib.BattleServer.SendBattle(card_id=value)

    def Pass(self):
        self.lib.BattleServer.SendBattle(system="Pass")
