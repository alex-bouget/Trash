import socket

class Serveur:
    def __init__(self):
        self.hote = ''
        self.port = 4862
        self.connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connexion_avec_client = 0
        self.infos_connexion = 0
        self.msg_recu = b""
        self.msg_envoi = b""
    def server_open(self):
        self.connexion_principale.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.connexion_principale.bind((self.hote, self.port))
        self.connexion_principale.listen(1)
        self.connexion_avec_client, self.infos_connexion = self.connexion_principale.accept()
    def server_stop(self):
        self.connexion_avec_client.close()
        self.connexion_principale.close()
    def server_send(self, msg_send):
        self.msg_envoi = str(msg_send)
        self.msg_envoi = self.msg_envoi.encode()
        self.connexion_avec_client.send(self.msg_envoi)
    def server_receive(self):
        self.msg_recu = self.connexion_avec_client.recv(1024)
        return self.msg_recu.decode()