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

        mouse_keys = pygame.mouse.get_pressed()
        if mouse_keys[0]:
            for button in menu.buttons:
                if button.clicked_over(pygame.mouse.get_pos()):
                    if button.text == "Easy":
                        return 1
                    elif button.text == "Medium":
                        return 2
                    elif button.text == "Hard":
                        return 3
                    elif button.text == "Exit":
                        return -1
        pygame.display.update()
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

    def draw_player(self, player):
        pygame.draw.rect(self.window, player.color, (player.position.x, player.position.y, player.size, player.size))

    def draw_scoreboard(self, score, highest_score):
        self.print_text("Score: " + str(score) + "   " + "Record: " + str(highest_score), (10, 505), 30, color.gray)

    def draw_time(self, time):
        self.print_text("Time: " + str(time), (350, 505), 30, color.gray)

    def draw_game_over(self):
        self.print_text("Game Over!", (100, 200), 60, color.red)
        pygame.display.update()
        time.sleep(2)

    def draw_wall(self, wall):
        wall.draw(self.window, color.white, pygame)
    
    def draw_ray(self, ray):
        ray.draw(self.window, color.white, pygame)

    def draw_rays(self, player, maze):
        vision_points = player.get_vision_rays(maze.walls_lines)
        for vision_point in vision_points:
            vision_point.draw(self.window, color.green, pygame)

    def refresh(self, maze, player, coin, score, time_left):
        self.window.fill(color.black)
        #self.draw_maze(maze)
        self.draw_player(player)
        #self.draw_coin(coin)
        #self.draw_scoreboard(score[0], score[1])
        #self.draw_time(time_left)
        self.draw_rays(player, maze)
        ray = Ray(Point(100, 250), Point(50,0))
        ray.set_direction(Point.from_tuple(pygame.mouse.get_pos()))
        self.draw_ray(ray)
        intersection_point = ray.cast(maze.walls_lines)
        if (intersection_point is not None):
            intersection_point.draw(self.window, color.green, pygame)
        pygame.display.update()






