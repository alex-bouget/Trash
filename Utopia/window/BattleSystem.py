from .Menu.Battle import GameCanvas
from .Menu.System.DeckChoiceSystem import DeckChoiceSys
from .Menu.Loading.BattleStartCanvas import BattleStartCanvas
import os
import logging
import json


class BattleSystem:
    def __init__(self, master, player_id, lib):
        self.game_canvas = GameCanvas(master, player_id,
                                      os.path.join(lib.Card.BddFolder, "font.ttf"),
                                      lib.Card.Model, lib.Card.Card.AllCard,
                                      {"Hand": self.Hand, "Board": self.Board, "Enemy": self.Enemy, "Pass": self.Pass})
        self.start_canvas = BattleStartCanvas(master, lib)
        self.Deck = DeckChoiceSys(master, "grey", lib.Deck.get_deck_name(), {"set": self.choice_deck},
                                  DeckChoiceSys.DeckSys)
        self.player_id = player_id
        self.lib = lib
        self.game_dict = {}
        self.battle_server = ""

    def startBattle(self, deck, battle_server):
        self.start_canvas.place(x=0, y=0)
        self.start_canvas.start(battle_server, self.player_id, deck)
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
            self.game_dict = self.start_canvas.ret
            self.game_canvas.change_battle(self.game_dict)
            self.lib.Server.BattleServer.GetBattle()
            self.looping2()
        else:
            self.start_canvas.after(500, self.looping1)

    def looping2(self):
        data = self.lib.Server.BattleServer.Get()
        if data is None:
            self.game_canvas.after(500, self.looping2)
        else:
            if self.game_dict != data:
                logging.debug("BattleSys: " + json.dumps(data))
                self.game_dict = data
                self.game_canvas.change_battle(data)
            self.lib.Server.BattleServer.GetBattle()
            self.game_canvas.after(500, self.looping2)

    def Hand(self, value):
        if self.game_dict["Phase"]["Phase"] == "Main" and self.game_dict["Phase"]["PlayerId"] == self.player_id:
            self.lib.Server.BattleServer.SendBattle(card_id=value)

    def Board(self, value):
        if (self.game_dict["Phase"]["Phase"] == "Battle" and self.game_dict["Phase"]["PlayerId"] == self.player_id) or (
                self.game_dict["Phase"]["Phase"] == "Def" and self.game_dict["Phase"]["PlayerId"] != self.player_id):
            self.lib.Server.BattleServer.SendBattle(card_id=value)

    def Enemy(self, value):
        if self.game_dict["Phase"]["Phase"] == "Destroy" and self.game_dict["Phase"]["PlayerId"] == self.player_id:
            self.lib.Server.BattleServer.SendBattle(card_id=value)

    def Pass(self):
        self.lib.Server.BattleServer.SendBattle(system="Pass")
