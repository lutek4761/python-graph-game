from game import Game
from menu import Menu
import pygame


class SceneManager:
    pygame.init()
    display = pygame.display.set_mode((800, 800))
    menu = Menu(display)
    game = Game(display)
    current_scene = menu

    @staticmethod
    def set_game_scene():
        SceneManager.current_scene = SceneManager.game

    @staticmethod
    def set_menu_scene():
        SceneManager.current_scene = SceneManager.menu

    # main linia 47
    @staticmethod
    def check_for_switch():
        if SceneManager.menu.set_game_scene:
            SceneManager.set_game_scene()
            SceneManager.menu.set_game_scene = False

        if SceneManager.game.set_menu_scene:
            SceneManager.set_menu_scene()
            SceneManager.game.set_menu_scene = False
