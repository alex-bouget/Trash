#-------------------------------------------------------------------------------
# Name:        Var_For_Var
# Purpose:     Script For Relic_Engine
#
# Author:      MisterMine01
#
# Created:     20/12/2019
# Copyright:   (c) MisterMine01 2019
#-------------------------------------------------------------------------------
def var_setup(self):
    try:
        self.var_var[0]
    except:
        self.var_var = []
        self.var_var.append("var_systeme")
        self.var_append("var_systeme", self.v)
def new_var(self, name_var):
    self.var_setup()
    try:
        self.var_index_name(name_var)
        raise NameError()
    except NameError:
        raise NameError("Alrealdy var as this name: "+str(name_var))
    except:
        self.var_var.append(str(name_var))
def var_append(self, name_var, enter):
    temp = self.var_var[self.var_index_name(name_var)]
    if type(enter) is list or type(enter) is tuple:
        self.var_var[self.var_index_name(name_var)] = temp+"*:/:*"+"*:/:*".join(enter)
    else:
        self.var_var[self.var_index_name(name_var)] = temp+"*:/:*"+str(enter)
def var_index_name(self, name_var):
    for i in range(len(self.var_var)):
        if self.var_var[i].split("*:/:*")[0]==str(name_var):
            return i
    raise "No Var has name: "+str(name_var)
def var_delete(self, name_var, index="ALL"):
    if index=="ALL":
        self.var_var[self.var_index_name(name_var)] = str(name_var)
    else:
        temp = self.var_var[self.var_index_name(str(name_var))].split("*:/:*")
        del temp[index+1]
        self.var_var[self.var_index_name(name_var)] = "*:/:*".join(temp)
def var_data(self, name_var, index="ALL"):
    temp = self.var_var[self.var_index_name(str(name_var))].split("*:/:*")
    del temp[0]
    if index=="ALL":
        return temp
    else:
        return temp[index]
def var_index(self, name_var, enter="ALL"):
    if enter=="ALL":
        return len(self.var_var[self.var_index_name(name_var)])
    else:
        return self.var_var[self.var_index_name(str(name_var))].split("*:/:*").index(enter)-1