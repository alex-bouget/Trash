from .ServerParent import Server
import json
from base64 import b64decode
import os
import logging


class AuthServ(Server):
    def __init__(self, url, folders):
        super().__init__(url)
        if not os.path.isdir(folders):
            os.mkdir(folders)
        self.ServerName = self.getJsBySystem("GetServId")["ServId"]
        self.folders = os.path.join(folders, self.ServerName)
        if not os.path.isdir(os.path.join(folders, self.ServerName)):
            os.mkdir(os.path.join(folders, self.ServerName))

    def TestBdd(self):
        def DownloadBdd(thread_self):
            logging.info("Download data")
            thread_self.thread_return.append("AuthServer.DownloadBDD.data.data")
            data = thread_self.getJsBySystem("GetBdd")
            open(os.path.join(thread_self.folders, "data.json"), "w").write(json.dumps(data))
            if not os.path.isdir(os.path.join(thread_self.folders, "rarity")):
                os.mkdir(os.path.join(thread_self.folders, "rarity"))
            for Name, dico in data["Rarity"].items():
                logging.info("Download Rarity " + Name)
                thread_self.thread_return.append("AuthServer.DownloadBDD.rarity." + Name)
                for Image in dico:
                    if Image != "head":
                        ex = thread_self.getJsBySystem("GetImage", {"imageType": "rarity", "idImage": Image})
                        if ex.get("Image") is not None:
                            open(os.path.join(thread_self.folders, "rarity", Image), "wb").write(b64decode(ex["Image"]))
            if not os.path.isdir(os.path.join(thread_self.folders, "head")):
                os.mkdir(os.path.join(thread_self.folders, "head"))
            for Image in data["Card"].keys():
                logging.info("Download Card Head " + Image)
                thread_self.thread_return.append("AuthServer.DownloadBDD.head." + Image)
                ex = thread_self.getJsBySystem("GetImage", {"imageType": "head", "idImage": Image + ".png"})
                if ex.get("Image") is not None:
                    open(os.path.join(thread_self.folders, "head", Image + ".png"), "wb").write(b64decode(ex["Image"]))
                else:
                    logging.warning(Image + "Head not found")
            logging.info("Download Font")
            thread_self.thread_return.append("AuthServer.DownloadBDD.font.Font")
            with open(os.path.join(thread_self.folders, "font.ttf"), "wb") as temp_file:
                temp_file.write(b64decode(thread_self.getJsBySystem("GetFont")["Font"]))
            with open(os.path.join(thread_self.folders, "v.json"), "w") as temp_file:
                temp_file.write(json.dumps(thread_self.getJsBySystem("GetBddVersion")))

        if os.path.isfile(os.path.join(self.folders, "v.json")):
            if json.load(open(os.path.join(self.folders, "v.json"))) != self.getJsBySystem("GetBddVersion"):
                DownloadBdd(self)
        else:
            DownloadBdd(self)

    def run(self):
        while self.GetSend() != "AuthServer.Start":
            pass
        self.thread_return.append("AuthServer.begin")
        while True:
            data = self.GetSend()
            if data == "AuthServer.End":
                self.thread_return.append("AuthServer.TaskFinish")
                break
            elif data == "AuthServer.TestBdd":
                self.TestBdd()
                self.thread_return.append("AuthServer.TestBddFinish")
            elif data == "AuthServer.ServerName":
                self.thread_return.append("AuthServer.ServerName." + self.ServerName)


def Auth_Server(url, folders):
    auth_serv = AuthServ(url, folders)
    auth_serv.start()
    return auth_serv.ThreadSend, auth_serv.ThreadReturn
