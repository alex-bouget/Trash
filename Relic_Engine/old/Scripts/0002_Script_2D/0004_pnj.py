#-------------------------------------------------------------------------------
# Name:        Pnj_2d
# Purpose:     Script For Relic_Engine
#
# Author:      MisterMine01
#
# Created:     03/04/2020
# Copyright:   (c) MisterMine01 2020
#-------------------------------------------------------------------------------
def pnj_2D(self, master):
    class pnj_2D:
        def __init__(self, master):
            self.root = master
            self.name_pnj = []
            self.all_pnj = []
            self.type = []
            self.all_Frame = []
            self.command = []
            self.coord = []
        def new_pnj(self, name, px, py, **args):
            if "image" in args:
                temp = Image.open(args["image"])
                if float(temp.size[0]/args["nb_Frame"]) != float(int(temp.size[0]/args["nb_Frame"])) or float(temp.size[1]/4) != float(int(temp.size[1]/4)):
                    raise ValueError("Number of frame unavailable with image size")
                temp3 = temp.size
                self.all_Frame.append([])
                x=0
                y=0
                for i in range(4):
                    temp2 = []
                    for i in range(args["nb_Frame"]):
                        temp2.append(ImageTk.PhotoImage(Image.open(args["image"]).crop((x*temp3[0]/args["nb_Frame"], y*temp3[1]/args["nb_Frame"], x*temp3[0]/args["nb_Frame"]+temp3[0]/args["nb_Frame"], y*temp3[1]/args["nb_Frame"]+temp3[1]/args["nb_Frame"]))))
                        x=x+1
                    x=0
                    y=y+1
                    self.all_Frame[-1].append(temp2)
                try:
                    tmp3 = self.root.hero.x.get()
                    tmp4 = self.root.hero.y.get()
                except:
                    tmp3=0
                    tmp4=0
                self.all_pnj.append(self.root.Map.create_image((px-tmp3)*self.root.Map.resolution+self.root.x//2+self.root.x_gap, (py-tmp4-1)*self.root.Map.resolution+self.root.Map.resolution//2+self.root.y//2+self.root.y_gap, image=self.all_Frame[-1][0][0]))
            else:
                self.all_pnj.append(None)
                self.all_Frame.append(None)
            self.coord.append([px,py])
            self.name_pnj.append(name)
            if "command" in args:
                self.command.append(args["command"])
            else:
                self.command.append(print)
            if "type" in args:
                if args["type"]=="pnj":
                    self.type.append("pnj")
                elif args["type"]=="trigger":
                    self.type.append("trigger")
                else:
                    print("args type invalid, processus "+name+" as a pnj")
                    self.type.append("pnj")
            else:
                self.type.append("pnj")
        def delete_pnj(self, name):
            if name=='all' or name=='ALL':
                for i in self.all_pnj:
                    self.root.Map.delete(i)
                self.all_pnj = []
                self.all_Frame = []
                self.command = []
                self.type = []
                self.coord = []
                self.name_pnj = []
            else:
                for i in range(len(self.name_pnj)):
                    if self.name_pnj[i]==name:
                        self.root.Map.delete(self.all_pnj[i])
                        del self.all_pnj[i]
                        del self.all_Frame[i]
                        del self.command[i]
                        del self.type[i]
                        del self.coord[i]
                for i in range(self.name_pnj.count(name)):
                    del self.name_pnj[self.name_pnj.index(name)]
        def teleport(self, name, x, y):
            if name in self.name_pnj:
                if self.all_pnj[self.name_pnj.index(name)]==None:
                    self.coord[self.name_pnj.index(name)] = [x, y]
                else:
                    try:
                        tmp3 = self.root.hero.x.get()
                        tmp4 = self.root.hero.y.get()
                    except:
                        tmp3=0
                        tmp4=0
                    xdiff = int(x)-int(self.coord[self.name_pnj.index(name)][0])
                    ydiff = int(y)-int(self.coord[self.name_pnj.index(name)][1])
                    self.root.Map.move(self.all_pnj[self.name_pnj.index(name)], self.root.Map.resolution*xdiff, self.root.Map.resolution*ydiff)
                    self.coord[self.name_pnj.index(name)] = [x, y]
            else:
                raise NameError(name+" is not created")
        def move_left(self, name):
            for i in range(int(self.root.Map.resolution/self.root.speed)):
                self.root.Map.move(self.all_pnj[self.name_pnj.index(name)], -self.root.speed, 0)
            self.coord[self.name_pnj.index(name)] = [self.coord[self.name_pnj.index(name)][0]-1, self.coord[self.name_pnj.index(name)][1]]
        def move_right(self, name):
            for i in range(int(self.root.Map.resolution/self.root.speed)):
                self.root.Map.move(self.all_pnj[self.name_pnj.index(name)], self.root.speed, 0)
            self.coord[self.name_pnj.index(name)] = [self.coord[self.name_pnj.index(name)][0]+1, self.coord[self.name_pnj.index(name)][1]]
        def move_up(self, name):
            for i in range(int(self.root.Map.resolution/self.root.speed)):
                self.root.Map.move(self.all_pnj[self.name_pnj.index(name)], 0, self.root.speed)
            self.coord[self.name_pnj.index(name)] = [self.coord[self.name_pnj.index(name)][0], self.coord[self.name_pnj.index(name)][1]-1]
        def move_down(self, name):
            for i in range(int(self.root.Map.resolution/self.root.speed)):
                self.root.Map.move(self.all_pnj[self.name_pnj.index(name)], 0, -self.root.speed)
            self.coord[self.name_pnj.index(name)] = [self.coord[self.name_pnj.index(name)][0], self.coord[self.name_pnj.index(name)][1]+1]
    return pnj_2D(master)