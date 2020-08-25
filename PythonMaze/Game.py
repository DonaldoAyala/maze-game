from Player import *
from Screen import *
from Menu import *
import Color as color


class Game:
	def __init__(self, width, height, cell_size):
		self.screen = Screen(width + 1, height + 1, color.black, "Maze Game")
		self.width = width
		self.height = height
		self.fps = 80
		self.running = True
		self.cell_size = cell_size
		self.clock = pygame.time.Clock()
		self.difficulty = 0

	def pressed_exit(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.quit()

	def quit(self):
		self.running = False

	def choose_difficulty(self):
		menu = Menu()
		while self.difficulty == 0:
			self.screen.draw_menu()

	def start(self):
		maze = Maze(self.width, self.height, self.cell_size)
		maze.generate()
		player = Player(maze.columns, maze.rows, 50)
		pygame.init()
		while self.running:
			self.clock.tick(self.fps)
			self.pressed_exit()
			player.move(maze)
			self.screen.refresh(maze, player)


if __name__ == "__main__":
	game = Game(500, 500, 100)
	game.start()
	pygame.quit()