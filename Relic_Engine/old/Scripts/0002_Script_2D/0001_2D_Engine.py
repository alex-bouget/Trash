#-------------------------------------------------------------------------------
# Name:        2d_Engine
# Purpose:     Script For Relic_Engine
#
# Author:      MisterMine01
#
# Created:     02/04/2020
# Copyright:   (c) MisterMine01 2020
#-------------------------------------------------------------------------------
exec("import threading")
def Engine_2D(self):
    class Engine_2D(Canvas):
        def __init__(self, master, x, y):
            self.root=master
            self.x=x
            self.y=y
            Canvas.__init__(self, self.root, width=self.x,height=self.y)
            self.place(x=0, y=0)
            self.speed=0.9
            self.x_gap = 0
            self.y_gap = 16
            self.Map = self.root.Map_2D(self, self.x, self.y)
            self.pnj = self.root.pnj_2D(self)
            self.root.E_0002 = self
        def load_hero(self, img, nb_Frame):
            self.hero = self.root.Hero_2D(self, img, nb_Frame)
        def move_left(self, *v):
            if [self.hero.x.get()-1, self.hero.y.get()] in self.Map.collision:
                self.Map.itemconfigure(self.hero.hero, image=self.hero.Frame_Hero[1][0])
            else:
                self.root.unbind_all()
                threading.Thread(target=self.hero.move_left).start()
                threading.Thread(target=self.Map.move_left).start()
        def move_right(self, *v):
            if [self.hero.x.get()+1, self.hero.y.get()] in self.Map.collision:
                self.Map.itemconfigure(self.hero.hero, image=self.hero.Frame_Hero[2][0])
            else:
                self.root.unbind_all()
                threading.Thread(target=self.hero.move_right).start()
                threading.Thread(target=self.Map.move_right).start()
        def move_up(self, *v):
            if [self.hero.x.get(), self.hero.y.get()-1] in self.Map.collision:
                self.Map.itemconfigure(self.hero.hero, image=self.hero.Frame_Hero[3][0])
            else:
                self.root.unbind_all()
                threading.Thread(target=self.hero.move_up).start()
                threading.Thread(target=self.Map.move_up).start()
        def move_down(self, *v):
            if [self.hero.x.get(), self.hero.y.get()+1] in self.Map.collision:
                self.Map.itemconfigure(self.hero.hero, image=self.hero.Frame_Hero[0][0])
            else:
                self.root.unbind_all()
                threading.Thread(target=self.hero.move_down).start()
                threading.Thread(target=self.Map.move_down).start()
        def play_pnj(self, *v):
            if [self.hero.x.get(), self.hero.y.get()] in self.pnj.coord:
                if self.Map.map_load[0] == "tmx_map":
                    self.pnj.command[self.pnj.coord.index([self.hero.x.get(), self.hero.y.get()])]()
                elif self.Map.map_load[0] == "relic_map":
                    self.pnj.command[self.pnj.coord.index([self.hero.x.get(), self.hero.y.get()])](self)
        def test_trigger(self, *v):
            if [self.hero.x.get(), self.hero.y.get()] in self.pnj.coord:
                if self.pnj.type[self.pnj.coord.index([self.hero.x.get(), self.hero.y.get()])] == "trigger":
                    if self.Map.map_load[0] == "tmx_map":
                        self.pnj.command[self.pnj.coord.index([self.hero.x.get(), self.hero.y.get()])]()
                    elif self.Map.map_load[0] == "relic_map":
                        self.pnj.command[self.pnj.coord.index([self.hero.x.get(), self.hero.y.get()])](self)
                else:
                    self.root.rebind_all()
            else:
                self.root.rebind_all()
    return Engine_2D(self, self.w, self.h)