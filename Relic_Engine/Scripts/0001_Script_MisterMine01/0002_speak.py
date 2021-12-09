#-------------------------------------------------------------------------------
# Name:        Speak
# Purpose:     Script For Relic_Engine
#
# Author:      MisterMine01
#
# Created:     20/08/2019
# Copyright:   (c) MisterMine01 2020
#-------------------------------------------------------------------------------
exec("import threading\nimport time",globals())
def write_speech(self):
    """return in self.txt, the text with delay for all letters"""
    systeme = list(self.var_data("0001_Script_MisterMine01/0002_speak", -1)) #list of letter to show
    for y in range(len(systeme)):
        d = [] #dictionary for show letters
        for i in range(y+1): #show letters
            if systeme[i] == "^":
                d.append("\n")
            else:
                d.append(systeme[i])
        self.txt.configure(text=str("".join(d)))
        time.sleep(0.025)
def speech(self, msg, back):
    """self.speech(msg, ft, back)"""
    try:
        self.new_var("0001_Script_MisterMine01/0002_speak")
    except:
        pass
    self.Msg = Canvas(self, width=self.w//1.5, height=self.h//4)
    self.txt = Label(self.Msg, text="", justify=LEFT)
    self.t1 = threading.Thread(target=self.write_speech)
    self.Msg.configure(bg=back)
    self.Msg.place(x=self.w//6, y=self.h-self.h//4)
    self.txt.configure(bg=back, font=(self.font,int(self.w//1.5//25)))
    self.var_append("0001_Script_MisterMine01/0002_speak", msg)
    self.txt.place(x=5, y=5)
    self.t1.start()
    self.unbind_all()
    self.root.bind('<Return>', self.speech_finish)
    self.root.mainloop()
def speech_finish(self, evt):
    """For finish speech"""
    if self.t1 == None:
        pass
    elif self.t1.isAlive() == False:
        self.using = False
        self.Msg.destroy()
        self.Msg = Canvas(self, width=self.w//1.5, height=self.h//4)
        self.txt = Label(self.Msg, text="")
        self.root.unbind('<Return>')
        self.rebind_all()
        if evt != "bonjour si vous voyez ce message vous n'avez gagne... BRAVO":
            self.root.quit()