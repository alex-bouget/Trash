import winsound as S
import playsound as P
class Music:
    def __init__(self):
        self.path = "song/"
        self.music = ""
        self.play_music = 1
        self.ambiant = 1
    def play(self, song, loop=False):
        if self.play_music ==1:
            self.music = song
            if loop:
                S.PlaySound(self.path+self.music+".wav", S.SND_LOOP + S.SND_ASYNC)
            else:
                S.PlaySound(self.path+self.music+".wav", S.SND_ASYNC)
    def stop(self):
        self.music = ""
        S.PlaySound(None, S.SND_PURGE)
    def play_ambiant(self, effect):
        if self.ambiant == 1:
            P.playsound(self.path+effect+".wav")