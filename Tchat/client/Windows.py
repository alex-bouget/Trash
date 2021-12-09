from tkinter import *
import api
import threading
from time import sleep

Client_Api = api.launch_api("ADD HERE IP ADRESS")


class connect_to_server(Canvas):
    def __init__(self, master):
        Canvas.__init__(self, master)
        Button(self, text="creer un compte", command=self.create).pack()
        Button(self, text="Se connecter", command=self.connect).pack()
    def create(self):
        data = Useless_Window.Useless_Asker().place("identifiant", "Nom du compte", "mot de passe", "répéter le\nmot de passe")
        if data["mot de passe"] == data["répéter le\nmot de passe"]:
            Client_Api.accounts.create_accounts(data["identifiant"], data["mot de passe"], data["Nom du compte"])
            self.quit()
    def connect(self):
        data = Useless_Window.Useless_Asker().place("identifiant", "mot de passe")
        Client_Api.accounts.connect_accounts(data["identifiant"], data["mot de passe"])
        self.quit()
    def _place(self, **kwargs):
        self.place(**kwargs)
        self.mainloop()
        return Client_Api.accounts.token
class discussion(Canvas):
    def __init__(self, master):
        Canvas.__init__(self, master)
        if "prof" in Client_Api.group.get_group(Client_Api.accounts.token):
            self.list = Listbox(self, height=380, width=720)
            self.list.place(x=0, y=0)
            self.data = []
            for group in Client_Api.group.get_group(Client_Api.accounts.token):
                self.list.insert(END, group)
                self.data.append(group_discussion(master, group))
            Button(self, text="creer un groupe").place(x=5, y=390)
            Button(self, text="ajouter au groupe").place(x=60, y=390)
            Button
        else:
            self.data = []
            self.list = Listbox(self, height=480, width=720)
            self.list.pack()
            for group in Client_Api.group.get_group(Client_Api.accounts.token):
                self.list.insert(END, group)
                self.data.append(group_discussion(master, group))
                self.list.bind('<<ListboxSelect>>', self.listt)
    def listt(self, evt):
        self.data[self.list.curselection()[0]]._place(x=0, y=0)


class group_discussion(Canvas):
    def __init__(self, master, discussion_name):
        self.data = []
        Canvas.__init__(self, master)
        self.name=discussion_name
        self.disc = Listbox(self, width=120, height=25)
        self.disc.grid(columnspan=3)
        Button(self, text="envoyer", command=self.send).grid(row=1, column=2)
        self.var = StringVar()
        Entry(self, textvariable=self.var).grid(row=1, column=1)
        Button(self, text="retour", command=self._place_forget).grid(row=1)
    def _place_forget(self):
        self.turn = False
        self.place_forget()
    def _place(self, **kwargs):
        self.place(**kwargs)
        self.turn=True
        threading.Thread(target=self.thread).start()
    def thread(self):
        while self.turn:
            try:
                for msg in Client_Api.group.get(self.name, len(self.data)):
                    self.disc.insert(END, msg[0]+": "+msg[1])
                    self.data.append(msg)
            except:
                pass
            sleep(3)
    def send(self):
        if self.var.get() != "":
            Client_Api.group.send_to(Client_Api.accounts.token, self.name, self.var.get())
            self.var.set("")




class Useless_Window:
    class Useless_Waiting:
        def __init__(self):
            self.root = Tk()
            self.root.title(lang[46])
        def place(self, msg):
            Label(self.root, text=msg).pack()
            self.root.mainloop()
        def destroy(self):
            self.root.destroy()
            self.root.quit()
    class Useless_Asker:
        def __init__(self, entre = True):
            self.root = Tk()
            self.entre=entre
            self.root.title("fenetre inutile")
            self.Enter = []
        def place(self, *kwargs):
            self.temp = []
            for key in kwargs:
                self.temp.append(key)
                Label(self.root, text=key).grid(row=len(self.temp)-1,column=0)
                if self.entre:
                    self.Enter.append(Entry(self.root))
                    if key=="mot de passe" or key=="répéter le\nmot de passe":
                        self.Enter[-1].configure(show="*")
                    self.Enter[-1].grid(row=len(self.temp)-1,column=1)
            Button(self.root, text="Terminer", command=self.butt).grid(row=len(self.temp),column=0)
            self.root.mainloop()
            if self.entre:
                return self.Return
        def butt(self):
            if self.entre:
                self.Return = {}
                for i in range(len(self.temp)):
                    self.Return[self.temp[i]] = self.Enter[i].get()
            self.root.quit()
            self.root.destroy()