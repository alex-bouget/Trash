import socket
class Client():
    def __init__(self):
        self.hote = ""
        self.port = 4862
        self.connexion_avec_serveur = 0
        self.msg_a_envoyer = b""
        self.msg_recu = b""
    def client_open(self, hote, port):
        self.hote = hote
        if port != "":
            self.port = int(port)
        self.connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connexion_avec_serveur.connect((self.hote, self.port))
    def client_close(self):
        self.connexion_avec_serveur.close()
    def client_send(self, msg):
       self.msg_a_envoyer =str(msg)
       self.msg_a_envoyer = self.msg_a_envoyer.encode()
       self.connexion_avec_serveur.send(self.msg_a_envoyer)
    def client_receive(self):
        self.msg_recu = self.connexion_avec_serveur.recv(1024)
        return self.msg_recu.decode()