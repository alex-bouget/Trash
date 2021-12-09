#-------------------------------------------------------------------------------
# Name:        Relic_Map
# Purpose:     Script For Relic_Engine
#
# Author:      MisterMine01
#
# Created:     09/05/2020
# Copyright:   (c) MisterMine01 2020
#-------------------------------------------------------------------------------
exec("import pytmx\nimport shutil\nimport xml.dom.minidom as minidom\nimport os\nimport zipfile",globals())
def Relic_Map(self, map_folder, tempdir=None):
    class RelicMap:
        def __init__(self, map_folder, tempdir):
            if zipfile.is_zipfile(map_folder)==False:
                if map_folder.split("/")[-1] != "":
                    map_folder = map_folder+"/"
                self.zip = False
            else:
                if tempdir.split("/")[-1] != "":
                    tempdir = tempdir+"/"
                self.zip = True
                self.tempdir = tempdir
            self.map_folder = map_folder
        def dir_file(self, file):
            t = file.split("/")
            del t[-1]
            return "/".join(t)
        def tree(self, rst):
            ret = []
            for i in os.listdir(rst):
                if os.path.isdir(rst+"/"+i):
                    for s in self.tree(rst+"/"+i):
                        ret.append(i+"/"+s)
                else:
                    ret.append(i)
            return(ret)
        def new_map(self, tmx):
            if self.zip:
                temp = zipfile.ZipFile(self.map_folder)
                temp.extractall(self.tempdir)
                self.delete_map(self.tempdir)
                self.create_map(tmx, self.tempdir)
                temp.close()
                temp = zipfile.ZipFile(self.map_folder, "w")
                for i in self.tree(self.tempdir):
                    temp.write(self.tempdir+i, i)
            else:
                self.delete_map(self.map_folder)
                self.create_map(tmx, self.map_folder)
        def delete_map(self, folder):
            if os.path.isfile(folder+"map"):
                for tsx in minidom.parse(folder+"map").getElementsByTagName("tileset"):
                    for png in minidom.parse(folder+tsx.getAttribute("source")).getElementsByTagName("image"):
                        os.remove(folder+png.getAttribute("source"))
                    os.remove(folder+tsx.getAttribute("source"))
                os.remove(folder+"map")
        def create_map(self, tmx, folder):
            shutil.copyfile(tmx, folder+tmx.split("/")[-1])
            try:
                os.mkdir(folder+"pnj_command")
                os.mkdir(folder+"pnj_img")
                os.mkdir(folder+"pnj_sprite")
            except:
                pass
            data = minidom.parse(folder+tmx.split("/")[-1])
            for tsx in data.getElementsByTagName("tileset"):
                shutil.copyfile(self.dir_file(tmx)+"/"+tsx.getAttribute("source"), folder+tsx.getAttribute("source").split("/")[-1])
                data2 = minidom.parse(self.dir_file(tmx)+"/"+tsx.getAttribute("source"))
                for png in data2.getElementsByTagName("image"):
                    shutil.copyfile(self.dir_file(tmx)+"/"+self.dir_file(tsx.getAttribute("source"))+"/"+png.getAttribute("source"), folder+png.getAttribute("source"))
                    png.setAttribute("source", png.getAttribute("source").split("/")[-1])
                tsx.setAttribute("source", tsx.getAttribute("source").split("/")[-1])
                open(folder+tsx.getAttribute("source").split("/")[-1], "w").write(data2.toprettyxml())
            open(folder+tmx.split("/")[-1], "w").write(data.toprettyxml())
            os.rename(folder+tmx.split("/")[-1], folder+"map")
            open(folder+"pnj_data", "w").close()
        def map_tmx(self):
            if self.zip:
                zipfile.ZipFile(self.map_folder).extractall(self.tempdir)
                return pytmx.TiledMap(self.tempdir+"map")
            else:
                return pytmx.TiledMap(self.map_folder+"map")
        def pnj(self):
            if self.zip:
                pnj = []
                zipfile.ZipFile(self.map_folder).extractall(self.tempdir)
                for i in open(self.tempdir+"pnj_data").read().split("\n"):
                    rt = []
                    rt.append(i.split("/")[0])
                    rt.append(i.split("/")[1])
                    rt.append([i.split("/")[3], i.split("/")[4]])
                    rt.append(i.split("/")[2])
                    if os.path.isfile(self.tempdir+"pnj_img/"+i.split("/")[0]):
                        rt.append(open(self.tempdir+"pnj_img/"+i.split("/")[0]).read().split("\n"))
                    else:
                        rt.append([None, None])
                    if os.path.isfile(self.tempdir+"pnj_command/"+i.split("/")[0]):
                        rt.append(open(self.tempdir+"pnj_command/"+i.split("/")[0]).read())
                    else:
                        rt.append("print")
                    pnj.append(rt)
                return pnj
            else:
                pnj = []
                for i in open(self.map_folder+"pnj_data").read().split("\n"):
                    rt = []
                    rt.append(i.split("/")[0])
                    rt.append(i.split("/")[1])
                    rt.append([i.split("/")[3], i.split("/")[4]])
                    rt.append(i.split("/")[2])
                    if os.path.isfile(self.map_folder+"pnj_img/"+i.split("/")[0]):
                        rt.append(open(self.map_folder+"pnj_img/"+i.split("/")[0]).read().split("\n"))
                    else:
                        rt.append([None, None])
                    if os.path.isfile(self.map_folder+"pnj_command/"+i.split("/")[0]):
                        rt.append(open(self.map_folder+"pnj_command/"+i.split("/")[0]).read())
                    else:
                        rt.append(None)
                    pnj.append(rt)
                return pnj
        def pnj_data(self, nb_data, name, x, y, pnj_type, img=None, frame=None, command=None):
            return [nb_data, name, [x, y], pnj_type, [img, frame], command]
            #[data, nom,[x,y],type,[img,nb_frame],command]
        def add_pnj(self, pnj_sys):
            if self.zip:
                zipfile.ZipFile(self.map_folder).extractall(self.tempdir)
                pnj_data = open(self.tempdir+"pnj_data").read()+"\n"+str(pnj_sys[0])+"/"+str(pnj_sys[1])+"/"+str(pnj_sys[3])+"/"+str(pnj_sys[2][0])+"/"+str(pnj_sys[2][1])
                open(self.tempdir+"pnj_data", "w").write(pnj_data)
            else:
                pnj_data = open(self.map_folder+"pnj_data").read()+"\n"+str(pnj_sys[0])+"/"+str(pnj_sys[1])+"/"+str(pnj_sys[3])+"/"+str(pnj_sys[2][0])+"/"+str(pnj_sys[2][1])
                open(self.map_folder+"pnj_data", "w").write(pnj_data)
                if pnj_sys[4][0]!=None and pnj_sys[4][1]!=None:
                    open(self.map_folder+"pnj_img/"+pnj_sys[0], "w").write(pnj_sys[4][0]+"\n"+pnj_sys[4][1])
                if pnj_sys[5]!=None:
                    open(self.map_folder+"pnj_command/"+pnj_sys[0], "w").write(pnj_sys[5])
        def return_dir(self):
            if self.zip:
                return self.tempdir
            else:
                return self.map_folder
    return RelicMap(map_folder, tempdir)