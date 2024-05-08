import pygame as pg
from settings import *

class ObjectRenderer:
    def __init__(self,game):
        self.game = game 
        self.screen = game.screen
        self.wall_texture = self.load_wall_texture()
    
    def draw(self):
        self.render_game_objects()    
    
    def render_game_objects(self):
        list_objects = self.game.raycasting.object_to_render
        for depth , image , pos in list_objects:
            self.screen.blit(image,pos)
            
        
            
    
    @staticmethod
    def get_texture(path,res=(TEXTURE_SIZE,TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture,res)
    
    def load_wall_texture(self):
        return{
            1: self.get_texture('resources/textures/1.png'),
            2: self.get_texture('resources/textures/wall.png'),  
            3: self.get_texture('resources/textures/3.png'),
            4: self.get_texture('resources/textures/4.png'),
            5: self.get_texture('resources/textures/5.png'),
        }