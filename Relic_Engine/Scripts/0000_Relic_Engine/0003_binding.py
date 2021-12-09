#-------------------------------------------------------------------------------
# Name:        Binding
# Purpose:     Script For Relic_Engine
#
# Author:      MisterMine01
#
# Created:     22/08/2019
# Copyright:   (c) MisterMine01 2020
#-------------------------------------------------------------------------------
def load_var_bind(self):
    try:
        self.new_var("0001_Script_MisterMine01/0003_bind")
    except:
        pass
    try:
        self.bind_function.reverse()
        self.bind_function.reverse()
    except:
        self.bind_function = []
def bind(self, touche, fonction):
    self.load_var_bind()
    for i in self.var_data("0001_Script_MisterMine01/0003_bind"):
        if i == touche:
            del self.bind_function[self.var_index("0001_Script_MisterMine01/0003_bind", touche)]
            self.var_delete("0001_Script_MisterMine01/0003_bind", self.var_index("0001_Script_MisterMine01/0003_bind", touche))
    self.root.bind(touche, fonction)
    self.var_append("0001_Script_MisterMine01/0003_bind", touche)
    self.bind_function.append(fonction)
def rebind_all(self):
    self.load_var_bind()
    for i in self.var_data("0001_Script_MisterMine01/0003_bind"):
        self.root.bind(i, self.bind_function[self.var_index("0001_Script_MisterMine01/0003_bind", i)])
def unbind_all(self):
    self.load_var_bind()
    for i in self.var_data("0001_Script_MisterMine01/0003_bind"):
        self.root.unbind(i)
def unbind(self, touche):
    self.load_var_bind()
    for i in self.var_data("0001_Script_MisterMine01/0003_bind"):
        if i == touche:
            del self.bind_function[self.var_index("0001_Script_MisterMine01/0003_bind", touche)]
            self.var_delete("0001_Script_MisterMine01/0003_bind", self.var_index("0001_Script_MisterMine01/0003_bind", touche))
    self.root.unbind(touche)