#Serveur Utopia 1.0

import socket
from threading import Thread
import select
import time
import sys
import UtopIa

hote = ''
port = 4862
class Systeme(Thread):
    def __init__(self, me):
        Thread.__init__(self)
        self.me = me
        self.ennemi = ''
        self.bot = False
        self.in_game = False
    def run(self):
        try:
            while True:
                msg_recu = self.me.recv(1024)
                msg_recu = msg_recu.decode()
                if msg_recu == "client£":
                    z = []
                    z.append("bot")
                    for i in clients_connectes:
                        if i != self.me:
                            if w[clients_connectes.index(i)].in_game == False:
                                z.append("Client "+str(clients_connectes.index(i)+1))
                    self.me.send((",".join(z)+"£").encode())
                else:
                    if msg_recu == "bot£":
                        Thread(target=lambda: UtopIa.call_ia("localhost", "", str(clients_connectes.index(self.me)+1), "deck")).start()
                        time.sleep(0.5)
                        self.ennemi = clients_connectes[-1]
                        self.bot = True
                        break
                    else:
                        r = msg_recu.split(" ")[1]
                        r = r.split("£")[0]
                        self.ennemi = clients_connectes[int(r)-1]
                        break
            print("<<CLIENT"+str(clients_connectes.index(self.me)+1)+">>: connection a CLIENT "+str(clients_connectes.index(self.ennemi)+1))
            while w[clients_connectes.index(self.ennemi)].ennemi == '':
                time.sleep(0.1)
            if w[clients_connectes.index(self.ennemi)].ennemi == self.me:
                self.me.send("bon£".encode())
                self.in_game = True
                time.sleep(3)
                while True:
                    msg_recu = self.me.recv(1024)
                    msg_recu = msg_recu.decode()
                    print("<<CLIENT"+str(clients_connectes.index(self.me)+1)+">>: |"+msg_recu+"|")
                    self.ennemi.send(msg_recu.encode())
            else:
                self.me.send("pas bon£".encode())
        except:
            print("<<CLIENT"+str(clients_connectes.index(self.me)+1)+">>: deconnection")
            del w[clients_connectes.index(self.me)]
            del clients_connectes[clients_connectes.index(self.me)]
            if self.bot == True:
                self.ennemi.close()

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
                                    if sd[1] == "battle" or sd[1] == "combat":
                                        if w[sd[2]-1].ennemi == '':
                                            print("CLIENT "+sd[2]+" ne se bat pas")
                                        else:
                                            print("CLIENT "+sd[2]+" se bat contre CLIENT "+str(clients_connectes.index(w[sd[2]-1].ennemi)+1))
                                    else:
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
w = []
while serveur_lance:
    connexions_demandees, wlist, xlist = select.select([connexion_principale],[], [], 0.05)
    for connexion in connexions_demandees:
        connexion_avec_client, infos_connexion = connexion.accept()
        clients_connectes.append(connexion_avec_client)
        print("une personne a rejoins")
        w.append(Systeme(connexion_avec_client))
        w[-1].start()