import pygame
import random
import color
import math

class Player:
	def __init__(self, columns, rows, size):
		self.pos_x = random.randint(0 ,columns - 1)
		self.pos_y = random.randint(0 ,rows - 1)
		self.speed = 10
		self.size = size

	def go_up(self):
		self.pos_y -= self.speed

	def go_right(self):
		self.pos_x += self.speed

	def go_down(self):
		self.pos_y += self.speed

	def go_left(self):
		self.pos_x -= self.speed

	def move(self, current_cell):
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT]:
			if current_cell.walls[3] and self.pos_x <= current_cell.col * current_cell.size:
				self.pos_x = current_cell.col * current_cell.size
			else:
				self.go_left()
		if key[pygame.K_RIGHT]:
			if current_cell.walls[1] and self.pos_x + self.size >= current_cell.col * current_cell.size + current_cell.size:
				self.pos_x = current_cell.col * current_cell.size + current_cell.size - self.size
			else:
				self.go_right()
		if key[pygame.K_DOWN]:
			if current_cell.walls[2] and self.pos_y + self.size >= current_cell.row * current_cell.size + current_cell.size:
				self.pos_y = current_cell.row * current_cell.size + current_cell.size - self.size
			else:
				self.go_down()
		if key[pygame.K_UP]:
			if current_cell.walls[0] and self.pos_y <= current_cell.row * current_cell.size:

				self.pos_y = current_cell.row * current_cell.size
			else:
				self.go_up()


class Screen:
	def __init__(self, width, height, color, caption):
		self.width = width
		self.height = height
		self.color = color
		self.caption = caption
		self.window = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption(self.caption)

	def draw_maze(self, maze):
		for i in range(maze.rows):
			for j in range(maze.columns):
				# maze.cells[i][j].draw_walls(self.window, maze.cell_size)
				if maze.cells[i][j].walls[0]:
					pygame.draw.line(self.window, color.white, (maze.cells[i][j].col * maze.cell_size ,maze.cells[i][j].row * maze.cell_size),
						(maze.cells[i][j].col * maze.cell_size + maze.cell_size,maze.cells[i][j].row * maze.cell_size))
				if maze.cells[i][j].walls[1]:
					pygame.draw.line(self.window, color.white, (maze.cells[i][j].col * maze.cell_size + maze.cell_size, maze.cells[i][j].row * maze.cell_size), (maze.cells[i][j].col * maze.cell_size + maze.cell_size,maze.cells[i][j].row * maze.cell_size + maze.cell_size))
				if maze.cells[i][j].walls[2]:
					pygame.draw.line(self.window, color.white, (maze.cells[i][j].col * maze.cell_size + maze.cell_size,maze.cells[i][j].row * maze.cell_size + maze.cell_size),(maze.cells[i][j].col * maze.cell_size,maze.cells[i][j].row * maze.cell_size + maze.cell_size))
				if maze.cells[i][j].walls[3]:
					pygame.draw.line(self.window, color.white, (maze.cells[i][j].col * maze.cell_size, maze.cells[i][j].row * maze.cell_size + maze.cell_size),(maze.cells[i][j].col * maze.cell_size, maze.cells[i][j].row * maze.cell_size))

	def draw_player(self, player):
		pygame.draw.rect(self.window, color.green, (player.pos_x, player.pos_y, player.size, player.size))

	def refresh(self, maze, player):
		self.window.fill(color.black)
		self.draw_maze(maze)
		self.draw_player(player)
		pygame.display.update()


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
			pygame.draw.line(win, color.white, (self.col * size, self.row * size),(self.col * size + size, self.row * size))
		if self.walls[1]:
			pygame.draw.line(win, color.white, (self.col * size + size, self.row * size),(self.col * size + size, self.row * size + size))
		if self.walls[2]:
			pygame.draw.line(win, color.white, (self.col * size + size, self.row * size + size),(self.col * size, self.row * size + size))
		if self.walls[3]:
			pygame.draw.line(win, color.white, (self.col * size, self.row * size + size),(self.col * size, self.row * size))


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
				print(self.cells[i][j], end=' || ')
			print("\n")
			print("----------------------------------------------")

	def generate(self):
		current_cell = self.cells[0][0]
		stack = [current_cell]
		while len(stack):
			current_cell = stack[-1]
			stack.pop()
			# print(self.has_neighbours(current_cell))
			if self.has_neighbours(current_cell):
				stack.append(current_cell)
			index = self.get_random_neighbour(current_cell)
			if index != -1:
				self.visit_cell(current_cell, self.moves[index])
				stack.append(
					self.cells[current_cell.col + self.moves[index][0]][current_cell.row + self.moves[index][1]])


class Game:

	def __init__(self, width, height, cell_size):
		self.screen = Screen(width + 1, height + 1, color.black, "Maze Game")
		self.width = width
		self.height = height
		self.fps = 80
		self.running = True
		self.cell_size = cell_size
		self.clock = pygame.time.Clock()

	def pressed_exit(self) -> bool:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True

	def quit(self):
		self.running = False

	def start(self):
		maze = Maze(self.width, self.height, self.cell_size)
		maze.generate()
		maze.print_maze()
		player = Player(maze.columns, maze.rows, 50)
		pygame.init()
		while self.running:
			self.clock.tick(self.fps)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
			player.move(maze.cells[math.floor(player.pos_x / maze.cell_size)][math.floor(player.pos_y / maze.cell_size)])
			self.screen.refresh(maze, player)


if __name__ == "__main__":
	game = Game(500, 500, 100)
	game.start()

"""
pygame.init()
screenWidth = 500
screenHeight = 500
win = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Maze")
x = 10
y = 10
width = 50
height = 50
vel = 5

run = True
while run:
	pygame.time.delay(10)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	win.fill((0,0,0))
	pygame.draw.rect(win,(255,0,0),(x,y,width,height))	
	pygame.display.update()
	key = pygame.key.get_pressed()
	if key[pygame.K_LEFT]:
		x -= vel
	if key[pygame.K_RIGHT]:
		x += vel
	if key[pygame.K_DOWN]:
		y += vel
	if key[pygame.K_UP]:
		y -= vel
	if x+width >= screenWidth:
		x = screenWidth - width
	if x <= 0:
		x = 0
	if y+height >= screenHeight:
		y = screenHeight - height
	if y <= 0:
		y = 0
"""
pygame.quit()