#-------------------------------------------------------------------------------
# Name:        Music
# Purpose:     Script For Relic_Engine
#
# Author:      MisterMine01
#
# Created:     08/08/2020
# Copyright:   (c) MisterMine01 2020
#-------------------------------------------------------------------------------
exec("import os\nimport vlc\nimport threading\nimport time", globals())

class Audio_Sortie:
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.song = []
        self.stop = True
        threading.Thread(target=self.loop).start()
    def start_song(self, file, repeat=True):
        self.stop = True
        self.song.append([file, repeat])
    def stop_song(self):
        self.stop = False
        self.player.stop()
    def volume(self, volume):
        self.player.audio_set_volume(volume)
    def loop(self):
        while True:
            if self.song != []:
                temp=self.song[0]
                del self.song[0]
                if temp[1]==True:
                    while self.stop:
                        if self.player.is_playing() == False:
                            self.player.set_media(self.instance.media_new(temp[0]))
                            self.player.play()
                            time.sleep(5)
                else:
                    self.player.set_media(self.instance.media_new(temp[0]))
                    self.player.play()