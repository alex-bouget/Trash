#-------------------------------------------------------------------------------
# Name:        Choice
# Purpose:     Script For Relic_Engine
#
# Author:      MisterMine01
#
# Created:     31/08/2019
# Copyright:   (c) MisterMine01 2019
#-------------------------------------------------------------------------------
def choice(self, *choice):
    """self.choice(*choice)"""
    if len(choice) > 10:
        print("more choice")
        exit
    choice = list(choice)
    msg = choice[0]
    choice.pop(0)
    back = choice[0]
    choice.pop(0)
    choice = tuple(choice)
    self.choice_choice = []
    self.choice_function = []
    self.choice_cursor = 0
    x = 0
    for i in range(len(choice)):
        if x == 0:
            self.choice_choice.append(choice[i])
            x = 1
        elif x ==1:
            self.choice_function.append(choice[i])
            x= 0
    if x == 1:
        print("no function")
        exit
    for i in range(len(self.choice_choice)):
        if i == 0:
            self.choice_c0 = Canvas(self, width=self.w//3, height=self.h//4.5)
            self.choice_c0.configure(bg=back)
            self.choice_L0 = Label(self.choice_c0, bg=back, text="\n".join(self.choice_choice[0].split("^")), font=("",int(self.w//1.5//25)))
            self.choice_L0.place(x=5, y=5)
            self.choice_c0.place(x=self.w-self.w//1.05 ,y=self.h-self.h//1.05)
        elif i == 1:
            self.choice_c1 = Canvas(self, width=self.w//3, height=self.h//4.5)
            self.choice_c1.configure(bg=back)
            self.choice_L1 = Label(self.choice_c1, bg=back, text="\n".join(self.choice_choice[1].split("^")), font=("",int(self.w//1.5//25)))
            self.choice_L1.place(x=5, y=5)
            self.choice_c1.place(x=self.w//1.65 ,y=self.h-self.h//1.05)
        elif i == 2:
            self.choice_c2 = Canvas(self, width=self.w//3, height=self.h//4.5)
            self.choice_c2.configure(bg=back)
            self.choice_L2 = Label(self.choice_c2, bg=back, text="\n".join(self.choice_choice[2].split("^")), font=("",int(self.w//1.5//25)))
            self.choice_L2.place(x=5, y=5)
            self.choice_c2.place(x=self.w-self.w//1.05 ,y=self.h//2.05)
        elif i == 3:
            self.choice_c3 = Canvas(self, width=self.w//3, height=self.h//4.5)
            self.choice_c3.configure(bg=back)
            self.choice_L3 = Label(self.choice_c3, bg=back, text="\n".join(self.choice_choice[3].split("^")), font=("",int(self.w//1.5//25)))
            self.choice_L3.place(x=5, y=5)
            self.choice_c3.place(x=self.w//1.65 ,y=self.h//2.05)
    self.curs = Canvas(self, width=self.w//20, height=self.h//20)
    self.curs.create_polygon((0, self.h//16, self.w//12.8, self.w//12.8, self.w//12.8, 0), fill="red")
    if msg != "":
        self.speech(msg,back)
    else:
        self.t1 = None
    self.root.unbind('<Return>')
    self.root.bind('<Left>', self.choice_cursor_l)
    self.root.bind('<Right>', self.choice_cursor_r)
    self.root.bind('<Up>', self.choice_cursor_u)
    self.root.bind('<Down>', self.choice_cursor_d)
    self.root.bind('<Return>', self.choice_finish)
    self.choice_cursor_move(1)
    self.root.mainloop()
def choice_cursor_l(self, evt):
    """for choice_cursor go to left"""
    self.choice_cursor_move(-1)
def choice_cursor_r(self, evt):
    """for choice_cursor go to right"""
    self.choice_cursor_move(1)
def choice_cursor_u(self, evt):
    """for choice_cursor go to up"""
    self.choice_cursor_move(-2)
def choice_cursor_d(self, evt):
    """for choice_cursor go to down"""
    self.choice_cursor_move(2)
def choice_cursor_move(self, plus):
    """for choice_cursor move"""
    if len(self.choice_choice) == 4:
        if plus == 2 and self.choice_cursor >=3:
            pass
        elif plus == 1 and self.choice_cursor == 4:
            pass
        elif plus == -2 and self.choice_cursor <=2:
            pass
        elif plus == -1 and self.choice_cursor ==1:
            pass
        else:
            self.choice_cursor = self.choice_cursor+plus
            if self.choice_cursor ==1:
                self.curs.place(x=self.w//51.2, y=self.h//32)
            elif self.choice_cursor == 2:
                self.curs.place(x=self.w//1.75, y=self.h//32)
            elif self.choice_cursor == 3:
                self.curs.place(x=self.w//51.2, y=self.h//2.15)
            elif self.choice_cursor == 4:
                self.curs.place(x=self.w//1.75,y=self.h//2.15)
    elif len(self.choice_choice) == 3:
        if plus == 2 and self.choice_cursor >= 2:
            pass
        elif plus == 1 and self.choice_cursoir == 3:
            pass
        elif plus == -2 and self.choice_cursor <= 2:
            pass
        elif plus == -1 and self.choice_cursor == 1:
            pass
        else:
            self.choice_cursor = self.choice_cursor+plus
            if self.choice_cursor ==1:
                self.curs.place(x=self.w//51.2, y=self.h//32)
            elif self.choice_cursor == 2:
                self.curs.place(x=self.w//1.75, y=self.h//32)
            elif self.choice_cursor == 3:
                self.curs.place(x=self.w//51.2, y=self.h//2.15)
    elif len(self.choice_choice) == 2:
        if plus == 2 and self.choice_cursor >= 1:
            pass
        elif plus == 1 and self.choice_cursor == 2:
            pass
        elif plus == -2 and self.choice_cursor <= 2:
            pass
        elif plus == -1 and self.choice_cursor == 1:
            pass
        else:
            self.choice_cursor = self.choice_cursor+plus
            if self.choice_cursor ==1:
                self.curs.place(x=self.w//51.2, y=self.h//32)
            elif self.choice_cursor == 2:
                self.curs.place(x=self.w//1.75, y=self.h//32)
    elif len(self.choice_choice) == 1:
        self.curs.place(x=self.w//51.2, y=self.h//32)
def choice_finish(self, evt):
    """For finish choice"""
    if self.t1==None or self.t1.isAlive() == False:
        self.using = False
        self.root.unbind('<Return>')
        self.root.unbind('<Left>')
        self.root.unbind('<Right>')
        self.root.unbind('<Up>')
        self.root.unbind('<Down>')
        for i in range(len(self.choice_choice)):
            exec("self.choice_c"+str(i)+".destroy()")
        self.curs.destroy()
        self.speech_finish("bonjour si vous voyez ce message vous avez gagne... BRAVO")
        self.choice_function[self.choice_cursor-1]()
        self.quit()
def choice_help(self):
    """View how to use choice()"""
    return "choice('msg','back_color','name of choice 1', function of choice 1, 'name of choice 2', ...)"