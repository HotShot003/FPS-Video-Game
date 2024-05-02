import pygame as pg
import sys
from settings import *

class Game:
    def __init__(self):
        pg.init()
        self.screen=pg.display.set_mode(RES)  #Initialize a window or screen for display
        self.clock=pg.time.Clock()  #create an object to help track time
        
    def new_game(self):    
        pass
    
    def update(self):
        pg.display.flip() #Update the full display Surface to the screen
        self.clock.tick(FPS) #update the clock
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')  #compute the clock framerate
        
    def draw(self):
        self.screen.fill('black')
        
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