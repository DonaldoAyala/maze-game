import pygame
import os
from Maze import *
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

	def center_window(self):
		os.environ['SDL_VIDEO_CENTERED'] = '0'

	def draw_coin(self, coin):
		pygame.draw.circle(self.window, color.yellow, coin.center, coin.radius)


	def draw_menu(self, menu):
		for button in menu.buttons:
			# Draw button rectangle
			pygame.draw.rect(self.window, button.color, button.position + button.size)
			# Create a font
			myfont = pygame.font.SysFont('franklingothicmedium', 20)
			# Get a text object
			text = myfont.render(button.text, True, color.black)
			self.window.blit(text, button.position + button.size)

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
					else:
						return 0
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
		pygame.draw.rect(self.window, color.gray, (player.pos_x, player.pos_y, player.size, player.size))

	def refresh(self, maze, player, coin):
		self.window.fill(color.black)
		self.draw_maze(maze)
		self.draw_player(player)
		self.draw_coin(coin)
		pygame.display.update()






