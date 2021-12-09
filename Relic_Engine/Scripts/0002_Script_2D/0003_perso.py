#-------------------------------------------------------------------------------
# Name:        Perso
# Purpose:     Script For Relic_Engine
#
# Author:      MisterMine01
#
# Created:     02/04/2020
# Copyright:   (c) MisterMine01 2020
#-------------------------------------------------------------------------------
exec("from PIL import Image, ImageTk\nimport threading\nimport time")
def Hero_2D(self, master, img, nb_Frame):
    class Hero_2D():
        def __init__(self, master, img, nb_Frame):
            self.root = master
            self.new_hero(img, nb_Frame)
            self.x = IntVar()
            self.y = IntVar()
            self.x.set(0)
            self.y.set(0)
            Label(self.root, textvariable=self.x).place(x=0,y=0)
            Label(self.root, textvariable=self.y).place(x=0,y=20)
        def new_hero(self, img, nb_Frame):
            try:
                self.root.Map.delete(self.hero)
            except:
                pass
            temp = Image.open(img)
            if float(temp.size[0]/nb_Frame) != float(int(temp.size[0]/nb_Frame)) or float(temp.size[1]/4) != float(int(temp.size[1]/4)):
                raise ValueError("Number of frame unavailable with image size")
            self.hauteur_sprite = temp.size[0]/nb_Frame
            self.largeur_sprite = temp.size[1]/nb_Frame
            self.nb_Frame = nb_Frame
            self.img = img
            self.Frame_Hero= [] # [DOWN, LEFT, RIGHT, UP]
            x=0
            y=0
            for i in range(4):
                temp2 = []
                for i in range(nb_Frame):
                    temp2.append(ImageTk.PhotoImage(Image.open(img).crop((x*self.hauteur_sprite, y*self.largeur_sprite, x*self.hauteur_sprite+self.hauteur_sprite, y*self.largeur_sprite+self.largeur_sprite))))
                    x=x+1
                x=0
                y=y+1
                self.Frame_Hero.append(temp2)
            self.Label_sys = False
            if self.Label_sys:
                self.hero = Label(self.root.Map, image=self.Frame_Hero[0][0])
                self.hero.place(x=self.root.x/2-self.largeur_sprite/2, y=self.root.y/2-self.hauteur_sprite/2)
            else:
                self.hero = self.root.Map.create_image(self.root.x/2, self.root.y/2, image=self.Frame_Hero[0][0])
            self.root.Map.set_hero(self.hero)
        def move_left(self, *v):
                threading.Thread(target= lambda: self.move_anim(self.Frame_Hero[1])).start()
                self.x.set(self.x.get()-1)
        def move_right(self, *v):
            threading.Thread(target= lambda: self.move_anim(self.Frame_Hero[2])).start()
            self.x.set(self.x.get()+1)
        def move_up(self, *v):
            threading.Thread(target= lambda: self.move_anim(self.Frame_Hero[3])).start()
            self.y.set(self.y.get()-1)
        def move_down(self, *v):
            threading.Thread(target= lambda: self.move_anim(self.Frame_Hero[0])).start()
            self.y.set(self.y.get()+1)
        def move_anim(self, anim):
            for i in anim:
                if self.Label_sys:
                    self.hero.configure(image=i)
                else:
                    self.root.Map.itemconfigure(self.hero, image=i)
                time.sleep((0.75/self.root.speed)/self.nb_Frame)
            if self.Label_sys:
                self.hero.configure(image=anim[0])
            else:
                self.root.Map.itemconfigure(self.hero, image=anim[0])
            time.sleep(0.1)
            self.root.test_trigger()
        def teleport(self, x, y):
            self.root.Map.move_map((self.x.get()-x)*self.root.Map.resolution, (self.y.get()-y)*self.root.Map.resolution)
            self.x.set(x)
            self.y.set(y)
    return Hero_2D(master, img, nb_Frame)