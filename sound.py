import pygame as pg


class Sound:
    def __init__(self,game):
        
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.shotgun = pg.mixer.Sound(self.path + 'm1-garand-rifle-80192.mp3')
        self.npc_pain = pg.mixer.Sound(self.path + 'man-death-scream.mp3')
        self.npc_death = pg.mixer.Sound(self.path + 'npc_death.wav')
        self.npc_shot = pg.mixer.Sound(self.path + 'npc_attack.wav')
        self.player_pain = pg.mixer.Sound(self.path + 'male-scream-in-fear.mp3')
        self.theme = pg.mixer.Sound(self.path + 'theme.mp3')