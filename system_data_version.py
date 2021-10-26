import os
v = "1.0.3" #version du jeu
v_enter = ["1.0.3", "1.0.2"] #version pouvant se connecter a ce client
if os.path.isfile("save/vers.txt")==False: #creation de fichier vers
    with open("save/vers.txt", "w") as f:
        f.write(v)
v_save = open("save/vers.txt").read()
if v!=v_save: #test d'un changement de version
    if os.path.isfile("save/vers.txt")==False: #reecriture du fichier de version
        with open("save/vers.txt", "w") as f:
            f.write(v)
if v_save == "1.0.3":
    if len(open("save/resolution.txt").read().split("\n")) != 2:
        temp = open("save/resolution.txt").read()
        open("save/resolution.txt", "w").write("yes\n"+temp)

mods_nb_enter = "µ"
mods_enter = " mods:"
if len(os.listdir("mods")) != 0: #test d'existance de mods
    v = v+mods_enter
    for i in os.listdir("mods"):
        v = v+" "+i