#-------------------------------------------------------------------------------
# Name:        Map
# Purpose:     Script For Relic_Engine
#
# Author:      MisterMine01
#
# Created:     02/04/2020
# Copyright:   (c) MisterMine01 2020
#-------------------------------------------------------------------------------
exec("import pytmx\nfrom PIL import Image, ImageTk\nimport time\nimport threading\nimport os", globals())
def Map_2D(self, master, x, y):
    class Map_2D(Canvas):
        def __init__(self, master, x, y):
            self.root=master
            self.x = x
            self.y=y
            Canvas.__init__(self, self.root, width=self.x,height=self.y)
            self.map_load = ""
            self.resolution = 0
            self.couche_collision = ""
            self.collision = []
            self.couche = []
            self.Map_sys = self.root.root.Map_sys()
            self.place(x=0, y=0)
            self.map_speed = self.root.speed+0.1
        def set_map_settings(self, **args):
            if "collision" in args:
                self.couche_collision = args["collision"]
            if "resolution" in args:
                self.resolution = args["resolution"]
            if "couche" in args:
                self.couche = []
                for i in args["couche"]:
                    self.couche.append(i)
            if "y" in args:
                self.root.y_gap=args["y"]
            if "x" in args:
                self.root.x_gap=args["x"]
            if "speed" in args:
                self.root.speed = args["speed"]
                self.map_speed = self.root.speed+0.1
        def load_tmx_map(self, tmx_file):
            tmp = pytmx.TiledMap(tmx_file)
            self.map_load = ["tmx_map", tmx_file]
            tmp2 = []
            for i in self.couche:
                tmp2.append(tmp.get_layer_by_name(str(i)).tiles())
            for u in tmp2:
                for x, y, image in u:
                    try:
                        self.root.root.unbind_all()
                    except:
                        pass
                    exec("self.Map_sys.x"+str(x)+"y"+str(y)+"=self.Map_sys.tiles_load(image[0], image[1])")
                    try:
                        tmp3 = self.root.hero.x.get()
                        tmp4 = self.root.hero.y.get()
                    except:
                        tmp3=0
                        tmp4=0
                    exec("self.Map_sys.image.append(self.create_image(self.resolution*(x-tmp3)+self.x//2+self.root.x_gap, self.resolution*(y-tmp4)+self.y//2+self.root.y_gap, image=self.Map_sys.x"+str(x)+"y"+str(y)+"))")
            try:
                self.root.hero.new_hero(self.root.hero.img, self.root.hero.nb_Frame)
            except:
                pass
            self.collision = []
            if self.couche_collision != "":
                for x, y, image in tmp.get_layer_by_name(self.couche_collision).tiles():
                    self.collision.append([x, y])
            self.root.root.rebind_all()
        def unload_map(self, *evt):
            self.delete(ALL)
            self.Map_sys.image = []
            self.root.pnj.delete_pnj("ALL")
        def load_relic_map(self, relic_folder, tempdir=None):
            relic_map = self.root.root.Relic_Map(relic_folder, tempdir)
            tmp = relic_map.map_tmx()
            self.map_load = ["relic_map", relic_folder]
            tmp2 = []
            for i in self.couche:
                tmp2.append(tmp.get_layer_by_name(str(i)).tiles())
            for u in tmp2:
                for x, y, image in u:
                    try:
                        self.root.root.unbind_all()
                    except:
                        pass
                    exec("self.Map_sys.x"+str(x)+"y"+str(y)+"=self.Map_sys.tiles_load(image[0], image[1])")
                    try:
                        tmp3 = self.root.hero.x.get()
                        tmp4 = self.root.hero.y.get()
                    except:
                        tmp3=0
                        tmp4=0
                    exec("self.Map_sys.image.append(self.create_image(self.resolution*(x-tmp3)+self.x//2+self.root.x_gap, self.resolution*(y-tmp4)+self.y//2+self.root.y_gap, image=self.Map_sys.x"+str(x)+"y"+str(y)+"))")
            try:
                self.root.hero.new_hero(self.root.hero.img, self.root.hero.nb_Frame)
            except:
                pass
            self.collision = []
            if self.couche_collision != "":
                for x, y, image in tmp.get_layer_by_name(self.couche_collision).tiles():
                    self.collision.append([x, y])
            for i in relic_map.pnj():
                if i[5]!=None:
                    temp2 = ["    "+tr for tr in i[5].split("\n")]
                    temp3 = {}
                    exec("def pnj_sys_"+i[0]+"(self):\n"+"\n".join(temp2), None, temp3)
                    for name, value in temp3.items():
                        setattr(self.root, name, value)
                    if i[4][0]==None or i[4][1]==None:
                        exec("self.root.pnj.new_pnj(i[1], int(i[2][0]), int(i[2][1]), type=i[3], command=self.root.pnj_sys_"+i[0]+")")
                    else:
                        exec('self.root.pnj.new_pnj(i[1], int(i[2][0]), int(i[2][1]), type=i[3], image=relic_map.return_dir()+"/sprite/"+i[4][0], nb_Frame=int(i[4][1]), command=self.root.pnj_sys_'+i[0]+')')
                else:
                    if i[4][0]==None or i[4][1]==None:
                        exec("self.root.pnj.new_pnj(i[1], int(i[2][0]), int(i[2][1]), type=i[3])")
                    else:
                        exec('self.root.pnj.new_pnj(i[1], int(i[2][0]), int(i[2][1]), type=i[3], image=relic_map.return_dir()+"/sprite/"+i[4][0], nb_Frame=int(i[4][1]))')
            self.root.root.rebind_all()
        def set_hero(self, hid):
            self.hero_id = hid
        def move_left(self, *v):
            threading.Thread(target= lambda: self.move_anim(self.resolution, 0)).start()
        def move_right(self, *v):
            threading.Thread(target= lambda: self.move_anim(-self.resolution, 0)).start()
        def move_up(self, *v):
            threading.Thread(target= lambda: self.move_anim(0, self.resolution)).start()
        def move_down(self, *v):
            threading.Thread(target= lambda: self.move_anim(0, -self.resolution)).start()
        def move_anim(self, x, y):
            if x < 0:
                xp=-x
            elif x==0:
                xp=None
            else:
                xp=x
            if y < 0:
                yp=-y
            elif y==0:
                yp=None
            else:
                yp=y
            if xp==None:
                if yp==None:
                    pass
                else:
                    for i in range(int(yp/self.map_speed)):
                        if y > 0:
                            self.move_map(0, self.map_speed)
                        else:
                            self.move_map(0, -self.map_speed)
                    if y > 0:
                        self.move_map(0, self.resolution-(int(yp/self.map_speed)*self.map_speed))
                    else:
                        self.move_map(0, -(self.resolution-(int(yp/self.map_speed)*self.map_speed)))
            elif yp==None:
                if xp==None:
                    pass
                else:
                    for i in range(int(xp/self.map_speed)):
                        if x > 0:
                            self.move_map(self.map_speed, 0)
                        else:
                            self.move_map(-self.map_speed, 0)
                    if x > 0:
                        self.move_map(self.resolution-(int(xp/self.map_speed)*self.map_speed), 0)
                    else:
                        self.move_map(-(self.resolution-(int(xp/self.map_speed)*self.map_speed)), 0)
        def move_map(self, x, y):
            self.move(ALL, x, y)
            self.move(self.hero_id, -x, -y)
    return Map_2D(master, x, y)
def Map_sys(self):
    class Map_sys:
        def __init__(self):
            self.tiles = []
            self.image = []
        def tiles_load(self, tileset, coord):
            temp1 = 0
            temp2 = 0
            for i in self.tiles:
                if i[0] == tileset:
                    for u in i:
                        if u == tileset:
                            pass
                        else:
                            if u[0] == coord:
                                return u[1]
                            else:
                                temp2 = temp2+1
                    temp3 = self.tiles.index(i)
                    self.tiles[temp3].append([coord, ImageTk.PhotoImage(Image.open(tileset).convert("RGBA").crop((coord[0], coord[1], coord[0]+coord[2], coord[1]+coord[3])))])
                    for i in self.tiles[temp3]:
                        if i[0] == coord:
                            return i[1]
                else:
                    temp1 = temp1+1
            self.tiles.append([tileset, [coord, ImageTk.PhotoImage(Image.open(tileset).convert("RGBA").crop((coord[0], coord[1], coord[0]+coord[2], coord[1]+coord[3])))]])
            return self.tiles[-1][1][1]
    return Map_sys()