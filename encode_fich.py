from encode import *
r = ["card/att.txt","card/def.txt","card/cout.txt","card/name.txt","card/nb.txt","card/effect.txt",]
for i in r:
    att = encodefich(i)
    f = open(i, "w")
    f.write(att)
    f.close()