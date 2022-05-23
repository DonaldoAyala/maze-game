import Color as color
from Scoreboard import *


class Menu:
    def __init__(self, best_score):
        self.texts = []
        self.texts.append(ScreenText("Lucky Maze", (125, 40), color.green, 50))
        self.texts.append(ScreenText("Fastest Game", (165, 100), color.green, 30))
        self.texts.append(ScreenText(str((best_score if best_score != -1 else '-')), (235, 140), color.yellow, 30))
        self.buttons = []
        # 'Medium difficulty button'
        self.buttons.append(Button((200, 210), (100, 30), color.gray, "Play", color.black))
        # Exit Button
        self.buttons.append(Button((10, 10), (50, 30), color.red, "Exit", color.white))

    def set_best_score(self, best_score):
        self.texts[2] = ScreenText(str(best_score), (235, 140), color.yellow, 30)


class ScreenText:

    def __init__(self, text, position, color, font_size):
        self.text = text
        self.position = position
        self.color = color
        self.font_size = font_size

class Button:

    def __init__(self, position, size, color, text, text_color):
        self.position = position
        self.size = size
        self.color = color
        self.text = text
        self.text_color = text_color

    def change_color(self, color):
        self.color = color

    def clicked_over(self, clicked_pos):
        if self.position[0] < clicked_pos[0] < self.position[0] + self.size[0] \
                and self.position[1] < clicked_pos[1] < self.position[1] + self.size[1]:
            return True
        else:
            return False