"""Lecteur de son pour Utopia creer par MisterMine01
Class Music"""
import winsound as S
import playsound as P
class Music:
    """Lecteur de son pour Utopia"""
    def __init__(self):
        self.path = "song/"
        self.music = ""
        self.play_music = 1
        self.ambiant = 1
    def play(self, song, loop=False):
        """jouer un son en arriere plan"""
        if self.play_music ==1:
            self.music = song
            if loop:
                S.PlaySound(self.path+self.music+".wav", S.SND_LOOP + S.SND_ASYNC)
            else:
                S.PlaySound(self.path+self.music+".wav", S.SND_ASYNC)
    def stop(self):
        """arreter le son en arriere plan"""
        self.music = ""
        S.PlaySound(None, S.SND_PURGE)
    def play_ambiant(self, effect):
        """bloque le jeu et joue un ambiant
        (a utilise de preference dans un Thread"""
        if self.ambiant == 1:
            P.playsound(self.path+effect+".wav")