import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *

class Game:
    def __init__(self):
        pg.init()
        self.screen=pg.display.set_mode(RES)  #Initialize a window or screen for display
        self.clock=pg.time.Clock()  #create an object to help track time
        self.delta_time=1
        self.new_game()
        
    def new_game(self):    
        self.map=Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
    def update(self):
        self.player.update()
        self.raycasting.update()
        pg.display.flip() #Update the full display Surface to the screen
        self.delta_time = self.clock.tick(FPS) #update the clock
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')  #compute the clock framerate
        
    def draw(self):
        self.screen.fill('black')
        self.object_renderer.draw()
        # self.map.draw()
        # self.player.draw()
        
    def check_events(self):
        for event in pg.event.get():
            if  event.type==pg.QUIT or (event.type == pg.KEYDOWN and event.key==pg.K_ESCAPE):
                pg.quit()  #uninitialize all pygame modules
                sys.exit() 
    
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()    
            
if __name__=='__main__':
    game=Game()
    game.new_game()
    game.run()
    