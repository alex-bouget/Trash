from .PrincipalSystem import Principal
from .Menu.AuthenticationCanvas import Authentication


class Game:
    def __init__(self, master, lib, battle_server):
        self.Authentication = Authentication(master, lib.Server.PrincipalServer)
        self.master = master
        self.lib = lib
        self.battle_server = battle_server
        self.loop1()

    def loop1(self):
        data = self.lib.Server.PrincipalServer.Get()
        if data is None:
            self.master.after(500, self.loop1)
        elif data == "PrincipalServer.Account.NotConnected":
            self.Authentication.place(x=0, y=0)
            self.Authentication.create_account.place(x=0, y=0)
            self.loop2()
        else:
            self.PrincipalMenu = Principal(self.master, data, self.lib, self.battle_server)
            self.PrincipalMenu.start()

    def loop2(self):
        data = self.lib.Server.PrincipalServer.Get()
        if data is None:
            self.master.after(500, self.loop2)
        elif (data == "PrincipalServer.Account.UserUse") or (data == "PrincipalServer.Account.NotConnected"):
            self.master.after(500, self.loop2)
            self.Authentication.changeInfo(data)
        else:
            self.PrincipalMenu = Principal(self.master, data, self.lib, self.battle_server)
            self.Authentication.place_forget()
            self.PrincipalMenu.start()
