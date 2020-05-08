import pygame
from pygame.locals import *
from game import Game
from menu import Menu

pygame.init()
display = pygame.display.set_mode((800, 800))
FPS = 1
delta = 0

game = Game()
menu = Menu()
clock = pygame.time.Clock()

while True:
    delta += clock.tick()
    if delta > 1000 / FPS:
        delta -= 1000 / FPS
    else:
        continue

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
        else:
            pass

    # if cos tam ...
    game.tick()
    game.draw()
    # else cos tam...
    menu.tick()
    menu.draw()
    pygame.display.update()
    display.fill([0, 0, 0])
