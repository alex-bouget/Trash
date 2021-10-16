"""Encodeur/Decodeur de MisterMine01
encode(string)
decode(string)
encode_fich(filename)
decode_fich(filename)
"""
enc = ['dx9b', 'gm2q', 'mp6h', 'fuze', 't6m0', 'km1h', '185d', 'klm0', 'lopf', 'l0pf', 'apdf', '1rfg', '9dru', '9ehb', '5zef', 'zef8', 'laae', 'rtfh', '85re', '9h1e', 'rz4r', 'ef8h', 'zer4', 'zrg7', 'yil4', 'uim9', '4ium', 'sv5b', 'dbu5', 'pmds', 'dfjk', '9r8b', '68qe', '9g4t', '6dth', 'gv6k', 'l9gp', 'for4', 'psm9', 'hpwm', 'lqz4', '1037', 'rev0', 'pq4m', 'lnth', 'l6td', '1po0', 'f2w9', '0ver', 'awpb', 'pqmo', '302k', 'lpq0', 'loq4', 'oq6p', 'mze3', 'zf5t', 'cow8', 'qq0m', 'qq1n', 'zs1m', 'apma', 'pvcd', 'msjc', '1047', 'mpoa', '10ed', 'mp15', 'qoa9', 'scos', 'dsvc', 'zovb', 'svkd', 'azer', 'sqcp', 'svcj', 'sqp8', 'sdf3', 'mq6j', 'pw3h', 'mds3', 'feci', 'fdps', 'dvge', 'dcnb', '601j', 'pd6g', 'rev3', 'md1q', 'dcsd', '', 'px4h', 'hgy5', 'gtz3', 'ths2', 'sfg4']
dec = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '/', '&', 'ÃƒÂ©', '"', "'", '(', '-', 'ÃƒÂ¨', '_', 'ÃƒÂ§', 'ÃƒÂ ', ')', '=', 'Ã‚Â°', '+', 'ÃƒÂ¯', 'Ã‚Â»', 'Ã‚Â¿', 'A', 'Z', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'Q', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'W', 'X', 'C', 'V', 'B', 'N', ':', '!', ';', ',', '?', '.', '/', 'Ã‚Â§', '\\', '\\n', '\\t', '<', '>', '[', ']']
def encode(string):
    """Encoder un texte"""
    decode = list(string)
    encode = []
    for sys in decode:
        if sys in dec:
            encode.append(enc[dec.index(sys)])
        else:
            print("caractere inconnue: "+sys)
    return "".join(encode)
def decode(string):
    """Decoder un texte"""
    encode = []
    encode1 = list(string)
    for i in range(len(encode1)//4):
        encode4 = encode1[i*4+0]+encode1[i*4+1]+encode1[i*4+2]+encode1[i*4+3]
        encode.append(encode4)
    decode = []
    for sys in encode:
        if sys in enc:
            decode.append(dec[enc.index(sys)])
        else:
            print("encodage inconnue: "+sys)
    return "".join(decode)
def encode_fich(filename):
    """Encoder un fichier"""
    with open(filename, "r") as fichier:
        return encode(fichier.read())
def decode_fich(filename):
    """Decoder un fichier"""
    encode = []
    with open(filename, "r") as fichier:
        return decode(fichier.read())
def ifencode(filename):
    """Tester si un fichier est encoder"""
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