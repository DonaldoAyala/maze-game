import pygame
import random
import Color as color


class Menu:
	def __init__(self):
		pass


class Button:

	def __init__(self, position, size, color):
		self.position = position
		self.size = size
		self.color = color

	def change_color(self, color):
		self.color = color

	def clicked_over(self, clicked_pos):
		if self.position[0] < clicked_pos[0] < self.position[0] + self.size[0] \
				and self.position[1] < clicked_pos[1] < self.position[1] + self.size[1]:
			return True
		else:
			return False


class Cell:
	def __init__(self, col, row, size):
		# Walls: 0:Up , 1:Right , 2:Bottom , 3:Left
		self.walls = [True, True, True, True]
		self.col = col
		self.row = row
		self.visited = False
		self.size = size

	def remove_wall(self, wall):
		self.walls[wall] = False

	def __str__(self):
		string = ""
		if self.walls[0]:
			string += 'u '
		if self.walls[1]:
			string += 'r '
		if self.walls[2]:
			string += 'b '
		if self.walls[3]:
			string += 'l '
		return string

	def draw_walls(self, win, size):
		self.size = size
		if self.walls[0]:
			pygame.draw.line(win, color.white, (self.col * size, self.row * size),
							 (self.col * size + size, self.row * size))
		if self.walls[1]:
			pygame.draw.line(win, color.white, (self.col * size + size, self.row * size),
							 (self.col * size + size, self.row * size + size))
		if self.walls[2]:
			pygame.draw.line(win, color.white, (self.col * size + size, self.row * size + size),
							 (self.col * size, self.row * size + size))
		if self.walls[3]:
			pygame.draw.line(win, color.white, (self.col * size, self.row * size + size),
							 (self.col * size, self.row * size))


class Maze:
	moves = [[0, -1], [1, 0], [0, 1], [-1, 0]]

	def __init__(self, screen_width, screen_height, cell_size):
		self.columns = round(screen_width / cell_size)
		self.rows = round(screen_height / cell_size)
		self.cell_size = cell_size
		self.cells = [[Cell(0, 0, cell_size)] * self.columns for i in range(self.rows)]
		for i in range(0, self.columns):
			for j in range(0, self.rows):
				self.cells[i][j] = Cell(i, j, cell_size)

	def is_valid(self, cell):
		if cell.col < 0 or cell.col >= self.columns:
			return False
		if cell.row < 0 or cell.row >= self.rows:
			return False
		if self.cells[cell.col][cell.row].visited:
			return False
		return True

	def has_neighbours(self, cell):
		for mv in self.moves:
			if self.is_valid(Cell(cell.col + mv[0], cell.row + mv[1], self.cell_size)):
				return True
		return False

	def visit_cell(self, cell, move):
		if not self.is_valid(Cell(cell.col + move[0], cell.row + move[1], self.cell_size)):
			return False
		if move == self.moves[0]:
			self.cells[cell.col][cell.row].remove_wall(0)  # Top
			self.cells[cell.col + move[0]][cell.row + move[1]].remove_wall(2)  # Bottom
		elif move == self.moves[1]:
			self.cells[cell.col][cell.row].remove_wall(1)  # Right
			self.cells[cell.col + move[0]][cell.row + move[1]].remove_wall(3)  # Left
		elif move == self.moves[2]:
			self.cells[cell.col][cell.row].remove_wall(2)  # Bottom
			self.cells[cell.col + move[0]][cell.row + move[1]].remove_wall(0)  # Top
		else:
			self.cells[cell.col][cell.row].remove_wall(3)  # Left
			self.cells[cell.col + move[0]][cell.row + move[1]].remove_wall(1)  # Right
		self.cells[cell.col + move[0]][cell.row + move[1]].visited = True
		return True

	def get_random_neighbour(self, cell):
		possible_moves = []
		for i in range(0, 4):
			if self.is_valid(Cell(cell.col + self.moves[i][0], cell.row + self.moves[i][1], self.cell_size)):
				possible_moves.append(i)
		if len(possible_moves):
			r = random.randint(1, len(possible_moves))
			return possible_moves[r - 1]
		return -1

	def print_maze(self):
		for i in range(self.rows):
			for j in range(self.columns):
				print(self.cells[j][i], end = ' || ')
			print("\n")
			print("----------------------------------------------")

	def generate(self):
		current_cell = self.cells[0][0]
		stack = [current_cell]
		while len(stack):
			current_cell = stack[-1]
			stack.pop()
			if self.has_neighbours(current_cell):
				stack.append(current_cell)
			index = self.get_random_neighbour(current_cell)
			if index != -1:
				self.visit_cell(current_cell, self.moves[index])
				stack.append(
					self.cells[current_cell.col + self.moves[index][0]][current_cell.row + self.moves[index][1]])