import pygame
from Player import *
from Screen import *
from Menu import *
import Color as color



class Game:
	def __init__(self, width, height, cell_size):
		self.screen = Screen(width + 1, height + 1, color.black, "Maze Game", )
		self.width = width
		self.height = height
		self.fps = 60
		self.running = True
		self.cell_size = cell_size
		self.clock = pygame.time.Clock()
		self.difficulty = 0
		pygame.init()

	def pressed_exit(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.quit()

	def quit(self):
		self.running = False

	def choose_difficulty(self):
		menu = Menu()
		while self.difficulty == 0 and self.running:
			self.clock.tick(self.fps)
			difficulty = self.screen.draw_menu(menu)
			if difficulty:
				self.difficulty = difficulty
			self.pressed_exit()

	def start(self):
		width, height, cell_size = 0,0,0
		player_size = 0
		if self.difficulty == 1:
			width, height, cell_size = 500, 500, 100
			player_size = 50
		elif self.difficulty == 2:
			width, height, cell_size = 500, 500, 50
			player_size = 30
		else:
			width, height, cell_size = 500, 500, 35
			player_size = 20
		maze = Maze(width, height, cell_size)
		maze.generate()
		player = Player(maze.columns, maze.rows, player_size)
		pygame.init()
		while self.running:
			self.clock.tick(self.fps)
			self.pressed_exit()
			player.move(maze)
			self.screen.refresh(maze, player)
