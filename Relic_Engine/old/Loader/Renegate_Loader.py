#-------------------------------------------------------------------------------
# Name:        Renegate_Loader
# Purpose:     Loaded Wanted Script For Relic_Engine
#
# Author:      MisterMine01
#
# Created:     09/05/2020
# Copyright:   (c) MisterMine01 2020
#-------------------------------------------------------------------------------
exec("from tkinter.ttk import Treeview\nimport tkinter.simpledialog as box", globals())
def loader_start():
    class Renegate_Loader():
        def __init__(self):
            self.root = Tk()
            self.root.configure(bg="blue")
            self.root.title("Renegate Loader")
            self.tree = Treeview(self.root)
            self.tree.grid()
            self.Can1 = Canvas(self.root, bg="grey")
            self.Can1.grid(column=1, row=0)
            self.type = StringVar()
            self.data = StringVar()
            self.button1 = StringVar()
            self.dic = []
            Label(self.Can1, textvariable=self.type, bg="grey").place(x=0, y=0)
            Label(self.Can1, textvariable=self.data, bg="grey").place(x=0, y=20)
            Button(self.Can1,textvariable=self.button1, bg="grey", command=self.button).place(x=0, y=240)
            Button(self.Can1, text="Start Engine", bg="grey", command=self.start).place(x=300, y=240)
            Button(self.Can1, text="Compile", bg="grey", command=self.compile).place(x=300,y=210)
        def start(self):
            load = []
            for i in self.dic:
                if i[2]==True:
                    load.append(open(i[1]).read())
            self.temp = "\n".join(load)
            self.root.destroy()
        def script_loaded(self):
            return [tr for tr in self.dic if tr[2]==True]
        def compile_module(self):
            impor = []
            for i in self.script_loaded():
                if i[0] != "0000_compile.py":
                    with open(i[1]) as r:
                        for az in r.read().split('\n'):
                            ar = az.split("(")
                            if ar[0] == "exec":
                                del ar[0]
                                at = "(".join(ar).split('"')
                                del at[0]
                                del at[-1]
                                impor.append('"'.join(at))
            impor_comp = []
            for i in impor:
                for x in i.split("\\n"):
                    impor_comp.append(x)
            impor_one = []
            for i in impor_comp:
                if i in impor_one:
                    pass
                else:
                    impor_one.append(i)
            return impor_one
        def compile_engine(self):
            Engin= []
            with open(__file__, "r") as Engine:
                for i in Engine.read().split("\n"):
                    if i == '    exec(open(loader).read())':
                        pass
                    else:
                        Engin.append(i)
            return Engin
        def compile_script(self):
            Script = []
            for i in self.script_loaded():
                if i[0] != "0000_compile.py":
                    Script.append('    #'+i[1].split("/")[1]+"/"+i[0])
                    with open(i[1]) as r:
                        for az in r.read().split('\n'):
                            ar = az.split("(")
                            if ar[0] != "exec":
                                Script.append("    "+az)
            return Script
        def compile(self):
            """compilation du moteur
            self.compile_engine(name)
            name=fichier de sortie de la compilation"""
            with open(box.askstring("name", "name of script"), "w") as output:
                output.write("\n".join(self.compile_module())+"\n"+"\n".join(self.compile_engine())+"\n"+"\n".join(self.compile_script()))
        def button(self):
            item = self.tree.selection()[0]
            if self.button1.get()=="Disable Script":
                for i in range(len(self.dic)):
                    if self.dic[i][0]==self.tree.item(item,"text") and self.dic[i][1]==self.tree.item(item,"values")[0]:
                        self.dic[i][2] = False
            elif self.button1.get()=="Enable Script":
                for i in range(len(self.dic)):
                    if self.dic[i][0]==self.tree.item(item,"text") and self.dic[i][1]==self.tree.item(item,"values")[0]:
                        self.dic[i][2] = True
            self.click("nique ta mère")
        def click(self, evt):
            item = self.tree.selection()[0]
            if self.tree.item(item,"values")[1]=="dir":
                self.type.set("types of "+self.tree.item(item,"text")+": dir")
                self.data.set("")
                self.button1.set("")
            else:
                self.type.set("types of "+self.tree.item(item,"text")+": file")
                temp = [rt[2] for rt in self.dic if rt[0]==self.tree.item(item,"text") and rt[1]==self.tree.item(item,"values")[0]][0]
                self.data.set("Script loaded: "+str(temp))
                if temp:
                    self.button1.set("Disable Script")
                else:
                    self.button1.set("Enable Script")
        def create_all(self):
            self.tree.heading("#0",text="Name",anchor=W)
            for i in os.listdir(script_dir):
                self.create_tree(self.tree, i)
            self.tree.bind("<Double-1>", self.click)
            self.tree.bind("<Return>", self.click)
        def create_tree(self, tree, directory, head=""):
            temp = tree.insert(head, END, text=directory.split("/")[-1], values=(script_dir+"/"+directory, "dir"))
            for i in os.listdir(script_dir+"/"+directory):
                if os.path.isdir(script_dir+"/"+directory+"/"+i):
                    self.create_tree(tree, directory+"/"+i, temp)
                else:
                    self.dic.append([i, script_dir+"/"+directory+"/"+i, True])
                    tree.insert(temp, END, text=i, values=(script_dir+"/"+directory+"/"+i, "file"))
        def run(self):
            self.create_all()
            self.root.mainloop()
            return self.temp
    return Renegate_Loader().run()
exec(loader_start())