#-------------------------------------------------------------------------------
# Name:        Mini_Script
# Purpose:     Script For Relic_Engine
#
# Author:      MisterMine01
#
# Created:     20/12/2019
# Copyright:   (c) MisterMine01 2020
#-------------------------------------------------------------------------------
exec("import PIL.ImageTk\nimport PIL.Image\nfrom urllib.request import *",globals())
def wait_game(self, time):
    self.root.after(int(time*1000), self.finish_wait)
    self.root.mainloop()
def finish_wait(self):
    self.root.quit()
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
    try:
        self.show_image_data.reverse()
        self.show_image_data.reverse()
    except:
            self.show_image_data = [[], []]
    self.show_image_data[0].append(nb)
    self.show_image_data[1].append(img)
    exec("self.I"+str(nb)+" = Label(self, image=self.show_image_data[1][-1])")
    exec("self.I"+str(nb)+".place(x=xn, y=yn)")
def destroy_image(self, nb):
    del self.show_image_data[1][self.show_image_data[0].index(nb)]
    del self.show_image_data[0][self.show_image_data[0].index(nb)]
    exec("self.I"+str(nb)+".destroy()")