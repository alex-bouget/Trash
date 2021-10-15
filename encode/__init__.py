#code a ne pas toucher
def decodesys(code):
    liste=[]
    mot=[]
    fichier = open("encode/enc.txt", "r")
    for sys in fichier:
        liste.append(sys[:-1])
    fichier.close()
    fichier2 = open("encode/dec.txt", "r")
    for sys2 in fichier2:
        mot.append(sys2[:-1])
    fichier.close()
    if code in liste:
        return mot[liste.index(code)]
    else:
        print('Erreur : votre encodage contient des caractere inconnu: '+code)
        exit
def encodesys(code):
    liste=[]
    mot=[]
    fichier = open("encode/enc.txt", "r")
    for sys in fichier:
        liste.append(sys[:-1])
    fichier.close()
    fichier2 = open("encode/dec.txt", "r")
    for sys2 in fichier2:
        mot.append(sys2[:-1])
    fichier.close()
    if code in mot:
        return liste[mot.index(code)]
    else:
        print('Erreur : votre encodage contient des caractere inconnu: '+code)
        exit
def encodefich(filename):
    fichier = open(filename, "r")
    ghlm = []
    for sys in fichier:
        sys = list(sys)
        while len(sys)>0:
            ghlm.append(sys[0])
            del sys[0]
    fichier.close()
    fin=[]
    for code in ghlm:
        fin.append(encodesys(code))
    d=[]
    for f in fin:
        if f != None:
            d.append(f)
    text2save = str("".join(d))
    return text2save
def decodefich(filename):
    fichier = open(filename, "r")
    fin=[]
    for sys in fichier:
        sys = list(sys)
        klao = []
        part = []
        while len(sys)>1:
            part.append(sys[0]+sys[1])
            del sys[0]
            del sys[0]
            part.append(sys[0]+sys[1])
            klao.append(part[0]+part[1])
            part = []
            del sys[0]
            del sys[0]
        for code in klao:
            fin.append(decodesys(code))
    fichier.close()
    text2save = str("".join(fin))
    return text2save