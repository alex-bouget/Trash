#-------------------------------------------------------------------------------
# Name:        Relic_Loader
# Purpose:     Loaded Script For Relic_Engine
#
# Author:      MisterMine01
#
# Created:     20/12/2019
# Copyright:   (c) MisterMine01 2020
#-------------------------------------------------------------------------------
def compile_module(self):
    impor = []
    for i in os.listdir(script_dir):
        for x in os.listdir(script_dir+"/"+i):
            if x != "0000_compile.py":
                with open(script_dir+"/"+i+"/"+x, "r") as r:
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
    for i in os.listdir(script_dir+"/"):
        for x in os.listdir(script_dir+"/"+i):
            if x != "0000_compile.py":
                Script.append('\n\n    #'+i+"/"+x+"\n\n")
                with open(script_dir+"/"+i+"/"+x, "r") as r:
                    for az in r.read().split('\n'):
                        ar = az.split("(")
                        if ar[0] != "exec":
                            Script.append("    "+az)
    return Script
def compile(self, name):
    """compilation du moteur
    self.compile_engine(name)
    name=fichier de sortie de la compilation"""
    with open(name, "w") as output:
        output.write("\n".join(self.compile_module())+"\n"+"\n".join(self.compile_engine())+"\n"+"\n".join(self.compile_script()))
if os.path.isdir(script_dir)==False:
    temp=script_dir.split("/")
    for i in range(len(temp)):
        temp2 = []
        for x in range(i+1):
            temp2.append(temp[x])
        temp3="/".join(temp2)
        if os.path.isdir(temp3)==False:
            os.mkdir(temp3)
for i in os.listdir(script_dir):
    for x in os.listdir(script_dir+"/"+i):
        with open(script_dir+"/"+i+"/"+x, "r") as r:
            exec(r.read())