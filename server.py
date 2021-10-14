#Serveur Card_Game 0.2

import socket
from threading import Thread
import select
import time
import sys

hote = ''
port = 4862
class Systeme(Thread):
    def __init__(self, me):
        Thread.__init__(self)
        self.me = me
    def run(self):
        while True:
            msg_recu = self.me.recv(1024)
            msg_recu = msg_recu.decode()
            print("<<CLIENT"+str(clients_connectes.index(self.me)+1)+">>: |"+msg_recu+"|")
            while len(clients_connectes) <= 1:
                time.sleep(0.1)
            for i in clients_connectes:
                if i != self.me:
                    i.send(msg_recu.encode())
class serveur(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.sys = True
    def run(self):
        while self.sys:
            sd = str(input())
            if sd == "stop" or sd == "exit":
                print("arret du serv")
                self.sys = False
                serveur_lance = False
                print("Fermeture des connexions")
                if clients_connectes != []:
                    for client in clients_connectes:
                        client.close()
                connexion_principale.close()
                sys.exit()
            else:
                try:
                    exec(sd)
                except:
                    if sd == "clients" or sd == "client":
                        print(str(len(clients_connectes))+" clients connectes")
                    elif sd == "help" or sd == "aide" or sd == "?":
                        print("client ou clients: Nombre de client connectes")
                        print("client X ou clients X: Informations du client X connectes")
                    else:
                        try:
                            sd = sd.split(" ")
                            if sd[0] == "client" or sd[0] == "clients":
                                try:
                                    print(str(clients_connectes[int(sd[1])]))
                                except:
                                    print("ce client n'existe pas")
                            else:
                                print("command inconnue (help)")
                        except:
                            print("command inconnue (help)")

m = serveur()
m.start()
connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)

serveur_lance = True
clients_connectes = []
client_sys = []
while serveur_lance:
    w = 0
    connexions_demandees, wlist, xlist = select.select([connexion_principale],
    [], [], 0.05)
    for connexion in connexions_demandees:
        connexion_avec_client, infos_connexion = connexion.accept()
        clients_connectes.append(connexion_avec_client)
        print("une personne a rejoins")
        w = Systeme(connexion_avec_client)
        w.start()