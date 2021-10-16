"""PyToPy creer par MisterMine01 avec socket
class Client
class Serveur"""
import socket
class Client():
    """Permet d'echanger des socket en tant que client
    self.client_open(hote, port)
    self.client_close()
    self.client_send(msg)
    self.client_receive()"""
    def __init__(self):
        self.hote = ""
        self.port = 4862
        self.connexion_avec_serveur = 0
        self.msg_a_envoyer = b""
        self.msg_recu = b""
    def client_open(self, hote, port):
        """Commencer une connection avec un serveur
        hote et port du serveur"""
        self.hote = hote
        if port != "":
            self.port = int(port)
        self.connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connexion_avec_serveur.connect((self.hote, self.port))
    def client_close(self):
        """Arreter la connection avec le serveur"""
        self.connexion_avec_serveur.close()
    def client_send(self, msg):
        """Envoyer des socket au serveur"""
        self.msg_a_envoyer =str(msg)
        self.msg_a_envoyer = self.msg_a_envoyer.encode()
        self.connexion_avec_serveur.send(self.msg_a_envoyer)
    def client_receive(self):
        """Attente d'un socket du serveur
        ATTENTION: BLOQUE LE SCRIPT (a faire dans un Thread de preference)"""
        self.msg_recu = self.connexion_avec_serveur.recv(1024)
        return self.msg_recu.decode()
class Serveur:
    """Permet d'echanger des socket en tant que serveur
    self.server_open(hote, port)
    self.server_close()
    self.server_send(msg)
    self.server_receive()"""
    def __init__(self):
        self.hote = ''
        self.port = 4862
        self.connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connexion_avec_client = 0
        self.infos_connexion = 0
        self.msg_recu = b""
        self.msg_envoi = b""
    def server_open(self):
        """Commencer a ecouter dans le port (self.port)"""
        self.connexion_principale.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.connexion_principale.bind((self.hote, self.port))
        self.connexion_principale.listen(1)
        self.connexion_avec_client, self.infos_connexion = self.connexion_principale.accept()
    def server_stop(self):
        """Arreter le serveur"""
        self.connexion_avec_client.close()
        self.connexion_principale.close()
    def server_send(self, msg_send):
        """Envoyer des socket au client"""
        self.msg_envoi = str(msg_send)
        self.msg_envoi = self.msg_envoi.encode()
        self.connexion_avec_client.send(self.msg_envoi)
    def server_receive(self):
        """Attente d'un socket du client
        ATTENTION: BLOQUE LE SCRIPT (a faire dans un Thread de preference)"""
        self.msg_recu = self.connexion_avec_client.recv(1024)
        return self.msg_recu.decode()