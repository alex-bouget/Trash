#-------------------------------------------------------------------------------
# Name:        Socket
# Purpose:     Script For Relic_Engine
#
# Author:      MisterMine01
#
# Created:     09/04/2020
# Copyright:   (c) MisterMine01 2020
#-------------------------------------------------------------------------------
exec("import socket\nimport threading\nimport pickle\nimport time",globals())
def Socket_start(self, host, port):
    self.Socket_host = host
    self.Socket_port = port
    self.Socket_connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.Socket_connect.connect((self.Socket_host, self.Socket_port))
    self.Socket_wheeling = True
    self.Socket_list = []
    threading.Thread(target=self.Socket_recup).start()
def Socket_recup(self):
    while self.Socket_wheeling:
        self.Socket_list.append(pickle.loads(self.Socket_connect.recv(4096)))
        print(self.Socket_list)
def Socket_receive(self, data):
    while len([sys for sys in self.Socket_list if sys[0]==data])==0:
        time.sleep(0.1)
    for i in self.Socket_list:
        if i[0] == data:
            temp = i
            break
    del self.Socket_list[self.Socket_list.index(i)]
    return i[1]
def Socket_Send(self, data, msg):
    self.Socket_connect.send(pickle.dumps([data, msg]))