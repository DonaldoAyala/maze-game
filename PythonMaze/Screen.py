import pygame
from Maze import *


class Screen:

	def __init__(self, width, height, color, caption):
		self.width = width
		self.height = height
		self.color = color
		self.caption = caption
		self.window = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption(self.caption)

	def draw_menu(self):
		button = Button((100, 100), (50, 50), color.blue)
		pygame.draw.rect(self.window, button.color, button.position + button.size)
		mouse_keys = pygame.mouse.get_pressed()
		if mouse_keys[0]:
			if button.clicked_over(pygame.mouse.get_pos()):
				print("Pressed over button")
		pygame.display.update()

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
		pygame.draw.rect(self.window, color.green, (player.pos_x, player.pos_y, player.size, player.size))

	def refresh(self, maze, player):
		self.window.fill(color.black)
		self.draw_maze(maze)
		self.draw_player(player)
		pygame.display.update()






