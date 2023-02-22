from ..System.VerticalSystem import VerticalSys
from .Card import Card


class HandCanvas(VerticalSys):
    def __init__(self, master, font_path, model, card, function):
        super().__init__(master)
        self.model = model
        self.old_dict = []
        self.CardSystem = card
        self.Card = []
        self.FontPath = font_path
        self.change_command(function)

    def change_command(self, function):
        for card in self.Card:
            card.configure(command=function)
        self.command = function

    def add_card(self, ide, card_image, attack, defence):
        self.Card.append(Card(self.Frame, ide, card_image, attack, defence, self.FontPath, False,
                              command=lambda card_id=ide: self.command(card_id)))
        self.Card[-1].pack()
        self.old_dict.append(ide)
        self.resize()

    def reload_Dict(self, game_dict):
        if game_dict != self.old_dict:
            def diff(first, second):
                def get_finish(listed):
                    finished = {}
                    for value in listed:
                        if value not in finished.keys():
                            finished[value] = 1
                        else:
                            finished[value] += 1
                    return finished

                first_finish = get_finish(first)
                second_finish = get_finish(second)
                for i in second_finish.keys():
                    if i in first_finish.keys():
                        first_finish[i] -= second_finish[i]
                        if first_finish[i] <= 0:
                            del first_finish[i]
                finish = []
                for i in first_finish.keys():
                    for x in range(first_finish[i]):
                        finish.append(i)
                return finish

            def sort_list(old_list, sorted_list):
                tuple_data = []
                for value in sorted_list:
                    tuple_data.append([])
                    for tuple_list in old_list:
                        if tuple_list[0] == value:
                            tuple_data[-1].append(tuple_list)
                finish = []
                for indexes in range(len(tuple_data)):
                    if len(tuple_data[indexes]) == 1:
                        finish.append(tuple_data[indexes][0])
                    else:
                        finish.append(tuple_data[indexes][sum(1 for old_n in tuple_data[:indexes]
                                                              if old_n[0][0] == tuple_data[indexes][0][0])])
                return finish

            for the_index in sorted([self.old_dict.index(card) for card in diff(self.old_dict, game_dict)],
                                    reverse=True):
                self.Card[the_index].destroy()
                del self.Card[the_index]
                del self.old_dict[the_index]

            for card in diff(game_dict, self.old_dict):
                self.add_card(card, self.model[card], self.CardSystem.getAtt(card), self.CardSystem.getDef(card))

            try:
                self.old_dict, self.Card = [list(listed) for listed in
                                            zip(*sort_list(list(zip(self.old_dict, self.Card)), game_dict))]
            except ValueError:
                pass
