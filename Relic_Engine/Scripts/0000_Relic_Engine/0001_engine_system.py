#-------------------------------------------------------------------------------
# Name:        Engine_System
# Purpose:     Script For Relic_Engine
#
# Author:      MisterMine01
#
# Created:     20/12/2019
# Copyright:   (c) MisterMine01 2019
#-------------------------------------------------------------------------------
def start_game(self):
    """Start game (mainloop)"""
    self.root.mainloop()
    self.stop_system()
def stop(self):
    self.root.destroy()
def stop_system(self):
    for i in self.stop_system_list:
        try:
            i()
        except:
            pass