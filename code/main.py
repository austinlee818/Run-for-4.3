import pygame,sys
from settings import *
from level import Level
from tiles import Tile

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
test_tile = pygame.sprite.Group(Tile((100,100),200))
clock = pygame.time.Clock()
level = Level(level_map,screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)