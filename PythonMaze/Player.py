import pygame
import math


class Player:
	def __init__(self, columns, rows, size):
		self.pos_x = 0
		self.pos_y = 0
		self.speed = 5
		self.size = size

	def go_up(self):
		self.pos_y -= self.speed

	def go_right(self):
		self.pos_x += self.speed

	def go_down(self):
		self.pos_y += self.speed

	def go_left(self):
		self.pos_x -= self.speed

	def move(self, maze):
		current_cell = maze.cells[math.floor(self.pos_x / maze.cell_size)][math.floor(self.pos_y / maze.cell_size)]
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
			if current_cell.walls[0] or ((up_right or right_up) and self.pos_x + self.size > (col + 1) * size):
				if self.pos_y <= row * size:
					self.pos_y = row * size
				else:
					self.go_up()
			else:
				self.go_up()
		if key[pygame.K_RIGHT]:
			if current_cell.walls[1] or ((right_bot or bot_right) and self.pos_y + self.size > (row + 1) * size):
				if self.pos_x + self.size >= (col + 1) * size:
					self.pos_x = (col + 1) * size - self.size
				else:
					self.go_right()
			else:
				self.go_right()
		if key[pygame.K_LEFT]:
			if current_cell.walls[3] or ((left_bot or bot_left) and self.pos_y + self.size > (row + 1) * size):
				if self.pos_x <= col * size:
					self.pos_x = col * size
				else:
					self.go_left()
			else:
				self.go_left()
		if key[pygame.K_DOWN]:
			if current_cell.walls[2] or ((right_bot or bot_right) and self.pos_x + self.size > (col + 1) * size):
				if self.pos_y + self.size >= (row + 1) * size:
					self.pos_y = (row + 1) * size - self.size
				else:
					self.go_down()
			else:
				self.go_down()