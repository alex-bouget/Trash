from .ServerParent import RcJsApi
import json
import os
import sys


class PrincipalServer(RcJsApi):
    def __init__(self, url, account_file, client_path):
        super().__init__(url)
        self.account_file = account_file
        self.client_path = client_path

    def start_client(self):
        if sys.argv[0].split(".")[-1] == "py":
            print("Dev mode: Allow Client connection to principal server ? y/other")
            if input(">>") != "y":
                print("token:")
                self.thread_return.append(input(">>"))
                return
        file = json.load(open(self.client_path))
        data = self.getJsBySystem("ConnectClient", {"ClientID": file["ClientID"], "C-Token": file["C-Token"]})
        if "Error" in data.keys():
            if data["Error"] == "Client not exist or bad token":
                raise OSError("Your game is not authenticate")
        else:
            file["C-Token"] = data["C-Token"]
            open(self.client_path, "w").write(json.dumps(file))
            if not os.path.isfile(self.account_file):
                self.thread_return.append("PrincipalServer.Account.NotConnected")
                return
            file = json.load(open(self.account_file))
            if any(ke in file for ke in ["Username", "A-Token"]):
                data = self.getJsBySystem("AutoConnectAccount", {"Username": file["Username"],
                                                                 "A-Token": file["A-Token"]})
                if "Error" in data.keys():
                    if data["Error"] == "Account not exist or bad token":
                        self.thread_return.append("PrincipalServer.Account.NotConnected")
                else:
                    file["A-Token"] = data["A-Token"]
                    self.thread_return.append(data["Token"])
            else:
                self.thread_return.append("PrincipalServer.Account.NotConnected")
            open(self.account_file, "w").write(json.dumps(file))

    def create_account(self, username, password):
        data = self.getJsBySystem("CreateAccount", {"Username": username, "Password": password})
        if "Error" in data.keys():
            if data["Error"] == "UserName Already Exist":
                self.thread_return.append("PrincipalServer.Account.UserUse")
        else:
            file = {"Username": data["UserName"], "A-Token": data["A-Token"]}
            self.thread_return.append(data["Token"])
            open(self.account_file, "w").write(json.dumps(file))

    def connect_account(self, username, password):
        data = self.getJsBySystem("ConnectAccount", {"Username": username, "Password": password})
        if "Error" in data.keys():
            if data["Error"] == "Account not exist or bad password":
                self.thread_return.append("PrincipalServer.Account.NotConnected")
        else:
            file = {"Username": data["UserName"], "A-Token": data["A-Token"]}
            self.thread_return.append(data["Token"])
            open(self.account_file, "w").write(json.dumps(file))

    def run(self):
        while self.GetSend() != "PrincipalServer.Start":
            pass
        self.thread_return.append("PrincipalServer.begin")
        self.start_client()
        while True:
            data = self.GetSend()
            if data == "PrincipalServer.CreateAccount":
                param = self.GetSend()
                self.create_account(param["username"], param["password"])
            elif data == "PrincipalServer.ConnectAccount":
                param = self.GetSend()
                self.connect_account(param["username"], param["password"])


def Principal_Server(url, account_file, client_path):
    principal_class = PrincipalServer(url, account_file, client_path)
    principal_class.start()
    return principal_class.ThreadSend, principal_class.ThreadReturn
