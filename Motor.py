import threading
import time
import winsound
import threading
import PIL.ImageTk
import PIL.Image
from urllib.request import *

script_dir = "Engine/Script"

"""Tkinter Engine Rpg"""
from tkinter import *
import ctypes
import os
usr32 = ctypes.windll.user32
all_fonction = []
class Engine(Canvas):
    """Tkinter Engine for rpg"""
    def __init__(self, title, w=usr32.GetSystemMetrics(0)//1.125, h=usr32.GetSystemMetrics(1)//1.125):
        self.w, self.h = w,h
        self.wt, self.ht = usr32.GetSystemMetrics(0)//1.125, usr32.GetSystemMetrics(1)//1.125
        self.root = Tk()
        self.root.geometry("%dx%d+0+0" % (self.w, self.h))
        Canvas.__init__(self, self.root)
        self.configure(width=self.wt, height=self.ht)
        self.root.title(title)
        self.using = False
        self.font = "times"
        self.color = "red"
    def start_game(self):
        """Start game (mainloop)"""
        self.place(x=0, y=0)
        self.root.mainloop()
    def stop(self):
        self.root.destroy()
    def all_function(self):
        """return all_function of script usable"""
        return('\n'.join(all_fonction))
    all_fonction.append("system function:")
    all_fonction.append("   start_game()")
    all_fonction.append("   all_function()")
    def write_speech(self):
        """return in self.txt, the text with delay for all letters"""
        l = [] #dictionary of all return of line
        for t in range(int(int(self.w//6)//int(self.w//1.5//25*2))+1):
            l.append(int(self.wt//1.5//25*(1.3*(t+1))))
        l.reverse()
        systeme = list(self.speak) #list of letter to show
        for y in range(len(systeme)):
            d = [] #dictionary for show letters
            for i in range(y+1): #show letters
                if systeme[i] == "^":
                    d.append("\n")
                else:
                    d.append(systeme[i])
            if self.return_line==True:
                for u in l: #return of line
                    if len(d) >= u:
                        d.insert(u, '\n')
            self.txt.configure(text=str("".join(d)))
            time.sleep(0.05)
    def speech(self, msg, back, return_line=True):
        """self.speech(msg, ft, back)"""
        try:
            self.msg_other.reverse()
            self.msg_other.reverse()
        except:
            self.msg_other = []
        if self.using == False:
            self.Msg = Canvas(self, width=self.w//1.5, height=self.h//4)
            self.txt = Label(self.Msg, text="")
            self.t1 = threading.Thread(target=self.write_speech)
            self.using = True
            self.return_line=return_line
            self.Msg.configure(bg=back)
            self.Msg.place(x=self.w//6, y=self.h-self.h//4)
            self.txt.configure(bg=back, font=(self.font,int(self.w//1.5//25)))
            self.speak = msg
            self.txt.place(x=5, y=5)
            self.t1.start()
            self.unbind_all()
            self.root.bind('<Return>', self.speech_finish)
        else:
            self.sys_again('self.speech("'+msg+'","'+back+'","'+str(return_line)+'")')
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
                self.again()
    all_fonction.append("speak function:")
    all_fonction.append("   speech(msg, font, background, return_line=True)")

    def choice(self, *choice):
        """self.choice(*choice)"""
        if self.using == False:
            if len(choice) > 9:
                print("more choice")
                exit
            if choice[0] == "use save":
                if choice[1] == "load save":
                    choice = self.choice_save[choice[2]]
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
            self.curs = Canvas(width=self.w//20, height=self.h//20)
            self.curs.create_polygon((0, self.h//16, self.w//12.8, self.w//12.8, self.w//12.8, 0), fill="red")
            for i in range(len(self.choice_choice)):
                if i == 0:
                    self.choice_c0 = Canvas(self, width=self.w//3, height=self.h//4.5)
                    self.choice_c0.configure(bg=back)
                    self.choice_L0 = Label(self.choice_c0, bg=back, text=self.choice_choice[0], font=("",int(self.w//1.5//25)))
                    self.choice_L0.place(x=5, y=5)
                    self.choice_c0.place(x=self.w-self.w//1.05 ,y=self.h-self.h//1.05)
                elif i == 1:
                    self.choice_c1 = Canvas(self, width=self.w//3, height=self.h//4.5)
                    self.choice_c1.configure(bg=back)
                    self.choice_L1 = Label(self.choice_c1, bg=back, text=self.choice_choice[1], font=("",int(self.w//1.5//25)))
                    self.choice_L1.place(x=5, y=5)
                    self.choice_c1.place(x=self.w//1.65 ,y=self.h-self.h//1.05)
                elif i == 2:
                    self.choice_c2 = Canvas(self, width=self.w//3, height=self.h//4.5)
                    self.choice_c2.configure(bg=back)
                    self.choice_L2 = Label(self.choice_c2, bg=back, text=self.choice_choice[2], font=("",int(self.w//1.5//25)))
                    self.choice_L2.place(x=5, y=5)
                    self.choice_c2.place(x=self.w-self.w//1.05 ,y=self.h//2.05)
                elif i == 3:
                    self.choice_c3 = Canvas(self, width=self.w//3, height=self.h//4.5)
                    self.choice_c3.configure(bg=back)
                    self.choice_L3 = Label(self.choice_c3, bg=back, text=self.choice_choice[3], font=("",int(self.w//1.5//25)))
                    self.choice_L3.place(x=5, y=5)
                    self.choice_c3.place(x=self.w//1.65 ,y=self.h//2.05)
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
            self.using == True
        else:
            try:
                self.choice_save.reverse()
                self.choice_save.reverse()
            except:
                self.choice_save = []
            self.choice_save.append(choice)
            self.sys_again('self.choice("use save", "load save",'+str(self.choice_save.index(choice))+')')
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
            self.again()
            self.choice_function[self.choice_cursor-1]()
    def choice_help(self):
        """View how to use choice()"""
        return "choice('msg','back_color','name of choice 1', function of choice 1, 'name of choice 2', ...)"
    all_fonction.append("choice_function:")
    all_fonction.append("   choice(*choice)")
    all_fonction.append("   choice_help()")

    def load_var_bind(self):
        try:
            self.bind_touche.reverse()
            self.bind_touche.reverse()
        except:
            self.bind_touche = []
        try:
            self.bind_function.reverse()
            self.bind_function.reverse()
        except:
            self.bind_function = []
    def bind(self, touche, fonction):
        self.load_var_bind()
        for i in self.bind_touche:
            if i == touche:
                del self.bind_function[self.bind_touche.index(i)]
                del self.bind_touche[self.bind_touche.index(i)]
        self.root.bind(touche, fonction)
        self.bind_touche.append(touche)
        self.bind_function.append(fonction)
    def rebind_all(self):
        self.load_var_bind()
        for i in self.bind_touche:
            self.root.bind(i, self.bind_function[self.bind_touche.index(i)])
    def unbind_all(self):
        self.load_var_bind()
        for i in self.bind_touche:
            self.root.unbind(i)
    def unbind(self, touche):
        self.load_var_bind()
        for i in self.bind_touche:
            if i == self.bind_touche:
                del self.bind_function[self.bind_touche.index(i)]
                del self.bind_touche[self.bind_touche.index(i)]
        self.root.unbind(touche)
    all_fonction.append("binding function:")
    all_fonction.append("   bind(touche, function)")
    all_fonction.append("   rebind_all()")
    all_fonction.append("   unbind_all()")
    all_fonction.append("   unbind(touche)")

    def sys_again(self, execute):
        try:
            self.list_again.reverse
            self.list_again.reverse
        except:
            self.list_again = []
        self.list_again.append(execute)
    def again(self):
        try:
            self.list_again.reverse
            self.list_again.reverse
        except:
            self.list_again = []
        if len(self.list_again) != 0:
            temp = self.list_again[0]
            del self.list_again[0]
            exec(temp)

    def play_music(self, music):
        """play music"""
        if self.using == False:
            winsound.PlaySound(music, winsound.SND_LOOP + winsound.SND_ASYNC)
            self.again()
        else:
            self.sys_again("self.play_music('"+music+"')")
    def stop_music(self):
        """stop music"""
        if self.using:
            self.sys_again("self.stop_music()")
        else:
            winsound.PlaySound(None, winsound.SND_PURGE)
            self.again()
    def stop_music_def(self):
        winsound.PlaySound(None, winsound.SND_PURGE)
    def play_ambient2(self, song):
        playsound(song)
    def play_ambient(self, song):
        if self.using == False:
            T = threading.Thread(target=self.play_ambient2(song))
            T.start()
            self.again()
        else:
            self.sys_again("self.play_ambient('"+song+"')")
    def wait_game(self, time):
        if self.using == False:
            self.using=True
            self.root.after(int(time*1000), self.finish_wait)
        else:
            self.sys_again("self.wait_game("+str(time)+")")
    def finish_wait(self):
        self.using=False
        self.again()
    def img(self, path, x=0, y=0):
        if x==0 or y==0:
            return PIL.ImageTk.PhotoImage(PIL.Image.open(path))
        else:
            return PIL.ImageTk.PhotoImage(PIL.Image.open(path).resize((x, y)))
    def img_bytes(self, path):
        return urlopen(Request(path, headers={'User-Agent': 'Mozilla/5.0'}))
    def show_image(self, img, nb, xn, yn):
        try:
            self.show_image_img.reverse()
            self.show_image_img.reverse()
        except:
            self.show_image_img = []
        if self.using:
            self.show_image_img.append(img)
            temp = len(self.show_image_img)-1
            self.sys_again("self.show_image(self.show_image_img["+str(temp)+"],"+str(nb)+","+str(xn)+","+str(yn)+")")
        else:
            exec("self.I"+str(nb)+" = Label(image=img)")
            exec("self.I"+str(nb)+".place(x=xn, y=yn)")
            self.again()
    def destroy_image(self, nb):
        if self.using:
            self.sys_again("self.destroy_image("+str(nb)+")")
        else:
            exec("self.I"+str(nb)+".destroy()")
            self.again()
