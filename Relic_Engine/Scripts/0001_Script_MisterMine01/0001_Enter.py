#-------------------------------------------------------------------------------
# Name:        Enter
# Purpose:     Script For Relic_Engine
#
# Author:      MisterMine01
#
# Created:     12/02/2020
# Copyright:   (c) MisterMine01 2020
#-------------------------------------------------------------------------------
def Enter(self):
    self.unbind_all()
    self.Enter_enter = Canvas(self, width=self.w//1.5, height=self.h//4, bg="red")
    self.Enter_enter.place(x=self.w//8, y=self.h//5)
    self.Enter_var = StringVar()
    self.Enter_label = Label(self.Enter_enter, textvariable=self.Enter_var, bg="red", font=("",int(self.w//1.5//25)))
    self.Enter_label.place(x=5, y=5)
    self.root.bind("<Key>", self.Enter_Key)
    self.root.mainloop()
    return self.Enter_wait
def Enter_Key(self, evt):
    if evt.keysym == "Return":
        self.Enter_finish()
    else:
        if evt.keysym == "BackSpace":
            r=list(self.Enter_var.get())
            del r[-1]
            self.Enter_var.set("".join(r))
        else:
            self.Enter_var.set(self.Enter_var.get()+str(evt.char))
def Enter_finish(self):
    self.Enter_enter.destroy()
    self.root.unbind("<Key>")
    self.rebind_all()
    self.Enter_wait = self.Enter_var.get()
    self.using=False
    self.root.quit()