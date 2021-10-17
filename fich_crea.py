import os

if os.path.isdir("deck")==False:
    os.mkdir("deck")
if os.path.isdir("mods")==False:
    os.mkdir("mods")
if os.path.isdir("save")==False:
    os.mkdir("save")
if os.path.isdir("save/options.txt")==False:
    with open("save/options.txt", "w") as f:
        f.write('1\n1')
if os.path.isfile("save/Dell.dat")==False:
    with open("save/Dell.dat", "w") as f:
        f.write("0")

if os.path.isfile("save/resolution.txt")==False:
    with open("save/resolution.txt", "w") as f:
        f.write("1080")