from .variables import Main, Camera
from .boot import on_boot

on_boot()

def Relic(name):
    Main.windows.title(name)
    return Main.relic_engine