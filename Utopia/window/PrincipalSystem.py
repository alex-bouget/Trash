from .Menu.Loading.StartCanvas import StartCanvas
from .Menu.PrincipalMenu import PrincipalMenu
from .BattleSystem import BattleSystem
from .DeckSystem import DeckSystem


class Principal:
    def __init__(self, master, player_id, lib, battle_server):
        self.battle_server = battle_server
        self.StartWindow = StartCanvas(master, lib)
        self.PrincipalMenu = PrincipalMenu(master, {"Play": self.start_battle,
                                                    "Deck": self.start_deck})
        self.BattleSys = BattleSystem(master, player_id, lib)
        self.DeckSys = DeckSystem(master, lib)

    def start_battle(self):
        self.BattleSys.starting(self.battle_server)

    def start_deck(self):
        self.DeckSys.start_deck()

    def start(self):
        self.StartWindow.place(x=0, y=0)
        self.StartWindow.start()
        self.test()

    def test(self):
        if self.StartWindow.StartFinish:
            self.DeckSys.DeckCanvas.EveryCard.set_card()
            self.StartWindow.wr.set("Creating Deck Model")
            self.StartWindow.update_idletasks()
            self.StartWindow.place_forget()
            self.PrincipalMenu.place(x=0, y=0)
        else:
            self.StartWindow.after(500, self.test)
