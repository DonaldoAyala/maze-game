from CoinGenerator import Coin
import pygame
import math
from Ray import *


class Player:
    def __init__(self, position, size, color, speed, rays_number):
        self.position = position
        self.speed = speed
        self.size = size
        self.color = color
        self.rays_number = rays_number
    
    def get_vision_rays(self, walls):
        angle_step = (2 * math.pi) / self.rays_number
        ray_length = 1
        i = 0
        vision_points = []
        while i < 2 * math.pi:
            x = ray_length * math.cos(i)
            y = ray_length * math.sin(i)
            ray = Ray(self.position, Point(x, y))
            vision_point = ray.cast(walls)
            if vision_point is not None:
                vision_points.append(vision_point)
            i += angle_step
        
        return vision_points

    def set_position(self, position):
        self.position = position

    def go_up(self):
        self.position.y -= self.speed

    def go_right(self):
        self.position.x += self.speed

    def go_down(self):
        self.position.y += self.speed

    def go_left(self):
        self.position.x -= self.speed

    def picked_coin(self, coin):
        player_center = (self.position.x + (self.size // 2), self.position.y + (self.size // 2))
        distance = ((player_center[0] - coin.center[0]) ** 2 + (player_center[1] - coin.center[1]) ** 2)**(1/2)
        return distance <= self.size // 2 + coin.radius

    def move(self, maze):
        current_cell = maze.cells[math.floor(self.position.x / maze.cell_size)][math.floor(self.position.y / maze.cell_size)]
        row, col = current_cell.row, current_cell.col
        size = current_cell.size
        bound = maze.rows
        up_right, right_bot, bot_left, bot_right, left_bot, right_up = False, False, False, False, False, False
        if row > 0:
            up_right = maze.cells[col][row - 1].walls[1]
        if col < bound - 1:
            right_bot = maze.cells[col + 1][row].walls[2]
            right_up = maze.cells[col + 1][row].walls[0]
        if row < bound - 1:
            bot_left = maze.cells[col][row + 1].walls[3]
            bot_right = maze.cells[col][row + 1].walls[1]
        if col > 0:
            left_bot = maze.cells[col - 1][row].walls[2]
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            if current_cell.walls[0] or ((up_right or right_up) and self.position.x + self.size > (col + 1) * size):
                if self.position.y <= row * size:
                    self.position.y = row * size
                else:
                    self.go_up()
            else:
                self.go_up()
        if key[pygame.K_RIGHT]:
            if current_cell.walls[1] or ((right_bot or bot_right) and self.position.y + self.size > (row + 1) * size):
                if self.position.x + self.size >= (col + 1) * size:
                    self.position.x = (col + 1) * size - self.size
                else:
                    self.go_right()
            else:
                self.go_right()
        if key[pygame.K_LEFT]:
            if current_cell.walls[3] or ((left_bot or bot_left) and self.position.y + self.size > (row + 1) * size):
                if self.position.x <= col * size:
                    self.position.x = col * size
                else:
                    self.go_left()
            else:
                self.go_left()
        if key[pygame.K_DOWN]:
            if current_cell.walls[2] or ((right_bot or bot_right) and self.position.x + self.size > (col + 1) * size):
                if self.position.y + self.size >= (row + 1) * size:
                    self.position.y = (row + 1) * size - self.size
                else:
                    self.go_down()
            else:
                self.go_down()






