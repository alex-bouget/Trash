enc = ['dx9b', 'gm2q', 'mp6h', 'fuze', 't6m0', 'km1h', '185d', 'klm0', 'lopf', 'l0pf', 'apdf', '1rfg', '9dru', '9ehb', '5zef', 'zef8', 'laae', 'rtfh', '85re', '9h1e', 'rz4r', 'ef8h', 'zer4', 'zrg7', 'yil4', 'uim9', '4ium', 'sv5b', 'dbu5', 'pmds', 'dfjk', '9r8b', '68qe', '9g4t', '6dth', 'gv6k', 'l9gp', 'for4', 'psm9', 'hpwm', 'lqz4', '1037', 'rev0', 'pq4m', 'lnth', 'l6td', '1po0', 'f2w9', '0ver', 'awpb', 'pqmo', '302k', 'lpq0', 'loq4', 'oq6p', 'mze3', 'zf5t', 'cow8', 'qq0m', 'qq1n', 'zs1m', 'apma', 'pvcd', 'msjc', '1047', 'mpoa', '10ed', 'mp15', 'qoa9', 'scos', 'dsvc', 'zovb', 'svkd', 'azer', 'sqcp', 'svcj', 'sqp8', 'sdf3', 'mq6j', 'pw3h', 'mds3', 'feci', 'fdps', 'dvge', 'dcnb', '601j', 'pd6g', 'rev3', 'md1q', 'dcsd', '', 'px4h', 'hgy5', 'gtz3', 'ths2', 'sfg4']
dec = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '/', '&', 'é', '"', "'", '(', '-', 'è', '_', 'ç', 'à', ')', '=', '°', '+', 'ï', '»', '¿', 'A', 'Z', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'Q', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'W', 'X', 'C', 'V', 'B', 'N', ':', '!', ';', ',', '?', '.', '/', '§', '\\', '\\n', '\\t', '<', '>', '[', ']']
#code a ne pas toucher
def decodesys(code):
    liste=enc
    mot=dec
    if code in liste:
        return mot[liste.index(code)]
    else:
        print('Erreur : votre encodage contient des caractere inconnu: '+code)
        return False
def encodesys(code):
    liste=enc
    mot=dec
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
            if decodesys(code) != False:
                fin.append(decodesys(code))
            else:
                return False
    fichier.close()
    text2save = str("".join(fin))
    return text2save
def ifencode(filename):
    try:
        liste=enc
        fichier = open(filename, "r")
        fin=[]
        for sys in fichier:
            sys = list(sys)
            klao = []
            part = []
            part.append(sys[0]+sys[1])
            del sys[0]
            del sys[0]
            part.append(sys[0]+sys[1])
            klao.append(part[0]+part[1])
            part = []
            del sys[0]
            del sys[0]
            if klao in liste:
                return False
            else:
                return True
    except:
        return False