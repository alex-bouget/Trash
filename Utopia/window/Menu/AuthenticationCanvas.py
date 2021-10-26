from tkinter import *
from ...Lang import getlang


class Connect(Canvas):
    def __init__(self, master, text, command):
        super().__init__(master)
        self.callback = command
        self.text_up = StringVar()
        self.data = {"username": StringVar(), "password": StringVar()}
        Label(self, textvariable=self.text_up).grid(row=0, column=0)
        Label(self, text="Username: ").grid(row=1, column=0)
        Entry(self, textvariable=self.data["username"]).grid(row=1, column=1)
        Label(self, text="Password: ").grid(row=2, column=0)
        Entry(self, textvariable=self.data["password"], show="*").grid(row=2, column=1)
        Button(self, text=text["B1"], command=self.Button1).grid(row=3, column=0, columnspan=2)
        Button(self, text=text["B2"], command=self.Button2).grid(row=4, column=0, columnspan=2)

    def Button1(self):
        self.callback["B1"](self.data)

    def Button2(self):
        self.callback["B2"](self.data)


class Authentication(Canvas):
    def __init__(self, master, lib):
        super().__init__(master)
        self.lib = lib
        self.create_account = Connect(self, {"B1": getlang()["AuthenticationCanvas"]["init"][0],
                                             "B2": getlang()["AuthenticationCanvas"]["init"][1]},
                                      {"B1": self.CreateAccount, "B2": self.pass_to_connect})
        self.connect_account = Connect(self, {"B1": getlang()["AuthenticationCanvas"]["init"][2],
                                              "B2": getlang()["AuthenticationCanvas"]["init"][3]},
                                       {"B1": self.login, "B2": self.pass_to_create})

    def changeInfo(self, text):
        self.create_account.text_up.set(text)
        self.connect_account.text_up.set(text)

    def pass_to_connect(self, data=None):
        self.create_account.place_forget()
        self.connect_account.place(x=int(self.winfo_width() // 2), y=int(self.winfo_height() // 2), anchor=CENTER)

    def pass_to_create(self, data=None):
        self.connect_account.place_forget()
        self.create_account.place(x=int(self.winfo_width() // 2), y=int(self.winfo_height() // 2), anchor=CENTER)

    def CreateAccount(self, data):
        self.lib.CreateAccount(data["username"].get(), data["password"].get())

    def login(self, data):
        self.lib.ConnectAccount(data["username"].get(), data["password"].get())

    def resize(self):
        self.configure(height=self.master.winfo_height(), width=self.master.winfo_width())
        if self.create_account.winfo_ismapped():
            self.create_account.place(x=int(self.winfo_width() // 2), y=int(self.winfo_height() // 2), anchor=CENTER)
        if self.connect_account.winfo_ismapped():
            self.connect_account.place(x=int(self.winfo_width() // 2), y=int(self.winfo_height() // 2), anchor=CENTER)
