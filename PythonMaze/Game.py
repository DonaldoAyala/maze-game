import pygame
from Player import *
from Screen import *
from Menu import *
from CoinGenerator import *
import Color as color


class Game:
	def __init__(self):
		self.screen = Screen(500 + 1, 500 + 1, color.black, "Maze Game")
		self.fps = 60
		self.running = True
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

	def set_difficulty(self):
		if self.difficulty == 1:
			return (500, 500, 100, 50)
		elif self.difficulty == 2:
			return (500, 500, 50, 30)
		else:
			return  (500, 500, 35, 20)

	def start(self):
		width, height, cell_size, player_size = self.set_difficulty()
		self.screen = Screen(width + 1, height + 1, color.black, "Maze Game")
		maze = Maze(width, height, cell_size)
		maze.generate()
		coin_generator = CoinGenerator((maze.columns, maze.rows), cell_size)
		coin = coin_generator.generate_coin()
		player = Player(player_size)
		while self.running:
			self.clock.tick(self.fps)
			self.pressed_exit()
			player.move(maze)
			self.screen.refresh(maze, player, coin)
