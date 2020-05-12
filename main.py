import pygame
from pygame.locals import *
from scene_manager import SceneManager


FPS = 30
delta = 0
up = False
down = False
enter = False
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                down = True
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_RETURN:
                enter = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                down = False
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_RETURN:
                enter = False

    SceneManager.current_scene.tick(up, down, enter)
    SceneManager.current_scene.draw()
    SceneManager.check_for_switch()
    pygame.display.update()
    SceneManager.display.fill([0, 0, 0])
