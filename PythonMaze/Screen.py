import pygame
import os
import time
from Maze import *
from Wall import *
from Ray import *
import Color as color


class Screen:

    def __init__(self, width, height, color, caption):
        self.width = width
        self.height = height
        self.center_window()
        self.color = color
        self.caption = caption
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)

    def print_text(self, text, position, font_size, color):
        my_font = pygame.font.SysFont('franklingothicmedium', font_size)
        local_text = my_font.render(text, True, color)
        self.window.blit(local_text, position + (len(text) * font_size + 5, font_size + 5))

    def center_window(self):
        os.environ['SDL_VIDEO_CENTERED'] = '0'

    def draw_coin(self, coin):
        pygame.draw.circle(self.window, color.yellow, coin.center, coin.radius )


    def draw_menu(self, menu):
        for text in menu.texts:
            self.print_text(text.text, text.position, text.font_size, text.color)
        for button in menu.buttons:
            pygame.draw.rect(self.window, button.color, button.position + button.size)
            self.print_text(button.text, button.position, 20, button.text_color)

        pygame.display.update()

        mouse_keys = pygame.mouse.get_pressed()
        if mouse_keys[0]:
            for button in menu.buttons:
                if button.clicked_over(pygame.mouse.get_pos()):
                    if button.text == "Play":
                        return 1
                    elif button.text == "Exit":
                        return -1
                    else:
                        return 0
        
        return 0

    def draw_maze(self, maze):
        for i in range(maze.rows):
            for j in range(maze.columns):
                if maze.cells[i][j].walls[0]:
                    pygame.draw.line(self.window, color.white,
                                     (maze.cells[i][j].col * maze.cell_size, maze.cells[i][j].row * maze.cell_size),
                                     (maze.cells[i][j].col * maze.cell_size + maze.cell_size,
                                      maze.cells[i][j].row * maze.cell_size))
                if maze.cells[i][j].walls[1]:
                    pygame.draw.line(self.window, color.white,
                                     (maze.cells[i][j].col * maze.cell_size + maze.cell_size,
                                      maze.cells[i][j].row * maze.cell_size),
                                     (maze.cells[i][j].col * maze.cell_size + maze.cell_size,
                                      maze.cells[i][j].row * maze.cell_size + maze.cell_size))
                if maze.cells[i][j].walls[2]:
                    pygame.draw.line(self.window, color.white,
                                     (maze.cells[i][j].col * maze.cell_size + maze.cell_size,
                                      maze.cells[i][j].row * maze.cell_size + maze.cell_size),
                                     (maze.cells[i][j].col * maze.cell_size,
                                      maze.cells[i][j].row * maze.cell_size + maze.cell_size))
                if maze.cells[i][j].walls[3]:
                    pygame.draw.line(self.window, color.white,
                                     (maze.cells[i][j].col * maze.cell_size,
                                      maze.cells[i][j].row * maze.cell_size + maze.cell_size),
                                     (maze.cells[i][j].col * maze.cell_size,
                                      maze.cells[i][j].row * maze.cell_size))

    def draw_exit_cell(self, exit_cell):
        pygame.draw.rect(self.window, color.red,
                        (exit_cell.col * exit_cell.size + 2, exit_cell.row * exit_cell.size + 2,
                        exit_cell.size - 2, exit_cell.size - 2))

    def draw_player(self, player):
        mid = player.size / 2
        pygame.draw.circle(self.window, player.color, (player.position + Point(mid, mid)).get_tuple(), player.size / 2)

    def draw_scoreboard(self, best_score):
        self.print_text("Best Time: " + str(best_score), (300, 505), 30, color.gray)

    def draw_time(self, time):
        self.print_text("Time: " + str(time), (10, 505), 30, color.gray)

    def draw_end_of_game(self):
        self.print_text("Finish!", (100, 200), 60, color.red)
        pygame.display.update()
        time.sleep(2)

    def draw_wall(self, wall):
        wall.draw(self.window, color.white, pygame)
    
    def draw_ray(self, ray):
        ray.draw(self.window, color.white, pygame)

    def draw_rays(self, player, maze):
        mid_point = Point(player.size / 2, player.size / 2)
        vision_points = player.get_vision_rays(maze.walls_lines)
        for vision_point in vision_points:
            pygame.draw.line(
                self.window, 
                color.gray, 
                (player.position + mid_point).get_tuple(), 
                vision_point.get_tuple())

    def refresh(self, maze, player, score, time):
        self.window.fill(color.black)
        #self.draw_maze(maze)
        #self.draw_player(player)
        self.draw_scoreboard(score)
        self.draw_time(time)
        self.draw_exit_cell(maze.exit_cell)
        self.draw_rays(player, maze)
        pygame.display.update()






