from .Menu.Battle import GameCanvas
from .Menu.System.DeckChoiceSystem import DeckChoiceSys
from .Menu.Loading.BattleStartCanvas import BattleStartCanvas
import os
import logging
import json
from tkinter.messagebox import showinfo
from ..Lang import getlang


class BattleSystem:
    def __init__(self, master, player_id, lib):
        self.game_canvas = GameCanvas(master, player_id,
                                      os.path.join(lib.Card.BddFolder, "font.ttf"),
                                      lib.Card.Model, lib.Card.Card.AllCard,
                                      {"Hand": self.Hand, "Board": self.Board, "Enemy": self.Enemy,
                                       "Pass": self.Pass, "Finish": self.Finish})
        self.start_canvas = BattleStartCanvas(master, lib)
        self.Deck = DeckChoiceSys(master, "grey", lib.Deck.get_deck_name(), {"set": self.choice_deck},
                                  DeckChoiceSys.DeckSys)
        self.player_id = player_id
        self.lib = lib
        self.game_dict = {}
        self.battle_server = ""

    def startBattle(self, deck):
        battle_id = "B1"
        # ici rajouter battle id canvas
        # BABABOY

        self.start_canvas.place(x=0, y=0)
        self.start_canvas.start(self.battle_server, self.player_id, deck, battle_id)
        self.looping1()

    def starting(self, battle_server):
        self.battle_server = battle_server
        self.Deck.ReloadFrame()
        self.Deck.place(x=0, y=0)

    def choice_deck(self, name):
        deck = self.lib.Deck.get_deck(name)
        if len(deck) < 20:
            showinfo(getlang()["BattleSystem"]["choice_deck"][0], getlang()["BattleSystem"]["choice_deck"][1])
        else:
            self.Deck.place_forget()
            self.startBattle(deck)

    def looping1(self):
        if self.start_canvas.StartFinish:
            self.start_canvas.place_forget()
            self.game_canvas.place(x=0, y=0)
            self.game_dict = self.start_canvas.ret
            self.game_canvas.change_battle(self.game_dict)
            self.lib.Server.BattleServer.GetBattle()
            self.lib.Discord.change_activity(state="on battle")
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
                get_finish = self.game_canvas.change_battle(data)
            else:
                get_finish = "ui"
            if get_finish != "Finish":
                self.lib.Server.BattleServer.GetBattle()
                self.game_canvas.after(500, self.looping2)
            else:
                self.game_canvas.place_forget()

    def sending_battle(self, value, board_id, phase_type):
        if self.game_dict["Phase"]["PhaseType"] in phase_type:
            if self.game_dict["Phase"]["PlayerId"] == self.player_id:
                if self.game_dict["Phase"]["PhaseUser"] == 0:
                    self.lib.Server.BattleServer.SendBattle(card_id=json.dumps({"card": value, "board_id": board_id}))
            elif self.game_dict["Phase"]["PhaseUser"] == 1:
                self.lib.Server.BattleServer.SendBattle(card_id=json.dumps({"card": value, "board_id": board_id}))

    def Hand(self, value):
        self.sending_battle(value, 0, [0, 3, 5, 6])

    def Board(self, value):
        self.sending_battle(value, 2, [2, 4, 5, 6])

    def Enemy(self, value):
        self.sending_battle(value, 1, [1, 3, 4, 6])

    def Pass(self):
        self.lib.Server.BattleServer.SendBattle(system="Pass")

    def Finish(self):
        self.lib.Server.BattleServer.StopServer()
