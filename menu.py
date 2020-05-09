from pygame import font
import pygame

class Menu:
    def __init__(self, display):
        font.init()
        self.display = display
        self.menu_font = font.Font('freesansbold.ttf', 32)
        self.selected_index = 0
        self.menu_text = ["Graj", "Zapisz", "Wyjdz"]
        self.blocker = False
        self.set_game_scene = False

    def tick(self, up, down, enter):
        if up and self.blocker:
            self.blocker = False
            if self.selected_index == 0:
                self.selected_index = len(self.menu_text) - 1
            else:
                self.selected_index -= 1
        elif not up and not self.blocker and not down and not enter:
            self.blocker = True

        if down and self.blocker:
            self.blocker = False
            if self.selected_index == len(self.menu_text) - 1:
                self.selected_index = 0
            else:
                self.selected_index += 1
        elif not down and not self.blocker and not up and not enter:
            self.blocker = True

        if enter and self.blocker:
            if self.selected_index == 0:
                self.set_game_scene = True
            elif self.selected_index == 1:
                pass # zapisz
            elif self.selected_index == 0:
                pygame.quit()
                exit(0)

            self.blocker = False
        elif not down and not self.blocker and not up and not enter:
            self.blocker = True

    def draw(self):
        for x in range(len(self.menu_text)):
            if self.selected_index == x:
                color = (0, 255, 0)
            else:
                color = (255, 255, 255)
            text = self.menu_font.render(self.menu_text[x], False, color)
            self.display.blit(text, (350, 40 * (x + 7)))
