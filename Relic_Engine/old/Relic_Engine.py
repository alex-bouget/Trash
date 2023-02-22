#-------------------------------------------------------------------------------
# Name:        Relic_Engine
# Purpose:     Engine For Create Game
#
# Author:      MisterMine01
#
# Created:     20/08/2019
# Copyright:   (c) MisterMine01 2020
#-------------------------------------------------------------------------------
script_dir = "Scripts"
loader = "Loader/Renegate_loader.py"

"""Tkinter Engine Rpg"""
from tkinter import *
import ctypes
import os
usr32 = ctypes.windll.user32
#Merci de ne pas touché a la dernières lignes (c'est pour la compilation)

class Engine(Canvas):
    """Tkinter Engine for rpg"""
    def __init__(self, title, w=usr32.GetSystemMetrics(0)//1.125, h=usr32.GetSystemMetrics(1)//1.125):
        self.v = "1.0"
        self.w, self.h = int(w),int(h)
        self.root = Tk()
        Canvas.__init__(self, self.root, width=self.w,height=self.h)
        self.place(x=0, y=0)
        self.root.title(title)
        self.root.configure(width=self.w,height=self.h)
        self.root.minsize(width=self.w, height=self.h)
        self.root.maxsize(width=self.w, height=self.h)
        self.using = False
        self.font = "times"
        self.color = "red"
        self.stop_system_list = []
    exec(open(loader).read())