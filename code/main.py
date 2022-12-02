import pygame,sys
from settings import *
from level import Level
from overworld import Overworld
from ui import UI

class Game:
    def __init__(self):
        self.max_level = 0
        self.health = 5
        self.coins = 0
        self.overworld = Overworld(0,self.max_level,screen,self.create_level)
        self.status = 'overworld'

        self.ui = UI(screen)

    def create_level(self,current_level):
        self.level = Level(current_level,screen,self.create_overworld,self.change_coins,self.change_health)
        self.status = 'level'

    def create_overworld(self,current_level,new_max_level):
        if new_max_level > self.max_level:
            self.max_level = new_max_level
        self.overworld = Overworld(current_level,self.max_level,screen,self.create_level)
        self.status = 'overworld'

    def change_coins(self,amount):
        self.coins += amount

    def change_health(self,amount):
        self.health += amount
    
    def check_game_over(self):
        if self.health <= 0:
            self.health = 5
            self.coins = 0
            self.max_level = 0
            self.overworld = Overworld(0,self.max_level,screen,self.create_level)
            self.status = 'overworld'

    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
        else:
            self.level.run()
            self.ui.show_health(self.health)
            self.ui.show_coins(self.coins)
            self.check_game_over()

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
game = Game()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    game.run()
    pygame.display.update()
    clock.tick(60)