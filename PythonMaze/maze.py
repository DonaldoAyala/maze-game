import pygame
import random
COLORS = {
	"WHITE" : (255, 255, 255),
	"BLACK" : (0, 0, 0),
	"RED" 	: (255, 0, 0),
	"GREEN" : (0, 255, 0),
	"BLUE"	: (0, 0, 255)
}


class Game:
	def __init__(self):
		self.screen = Screen(200, 200, COLORS["BLACK"], "Maze Game")

	def start(self):
		clock = pygame.time.Clock()
		fps = 60
		pygame.init()
		run = True
		while run:
			clock.tick(fps)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
			pygame.display.update()
			keys = pygame.key.get_pressed()


class Screen:
	def __init__(self, width, height, color, caption):
		self.width = width
		self.height = height
		self.color = color
		self.caption = caption
		self.window = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption(self.caption)

	def draw_maze(self, maze):
		pass


class Maze:
	moves = [[0, -1], [1, 0], [0, 1], [-1, 0]]
	def __init__(self, screen_width, screen_height, cell_size):
		self.columns = round(screen_width / cell_size)
		self.rows = round(screen_height / cell_size)
		self.cells = [[Cell(int(0), int(0))] * self.columns for i in range(self.rows)]
		for i in range(self.columns):
			for j in range(self.rows):
				self.cells[i][j].x = i * cell_size
				self.cells[i][j].y = j * cell_size

	def is_valid(self, cell):
		if cell.x < 0 or cell.x >= self.columns:
			return False
		if cell.y < 0 or cell.y >= self.rows:
			return False
		if self.cells[cell.x][cell.y].visited:
			return False
		return True

	def has_neighbours(self, cell):
		for mv in self.moves:
			if self.is_valid(Cell(cell.x + mv[0], cell.y + mv[1])) :
				return True
			return False

	def visit_cell(self, cell, move):
		if not self.is_valid(Cell(cell.x + move[0], cell.y + move[1])):
			return False
		if move == self.moves[0]:
			self.cells[cell.x][cell.y].remove_wall(0) # Top
			self.cells[cell.x + move[0]][cell.y + move[1]].remove_wall(2) # Bottom
		elif move == self.moves[1]:
			self.cells[cell.x][cell.y].remove_wall(1) # Right
			self.cells[cell.x + move[0]][cell.y + move[1]].remove_wall(3) # Left
		elif move == self.moves[2]:
			self.cells[cell.x][cell.y].remove_wall(2) # Bottom
			self.cells[cell.x + move[0]][cell.y + move[1]].remove_wall(0) # Top
		else:
			self.cells[cell.x][cell.y].remove_wall(3) # Left
			self.cells[cell.x + move[0]][cell.y + move[1]].remove_wall(1) # Right
		self.cells[cell.x + move[0]][cell.y + move[1]].visited = True
		return True

	def get_random_neighbour(self, cell):
		possible_moves = []
		for i in range(0, 4):
			if self.is_valid(Cell(cell.x + self.moves[i][0], cell.y + self.moves[i][1])):
				possible_moves.append(i)
		r = random.randint(0, lxen(possible_moves))
		if len(possible_moves):
			return possible_moves[r]
		return -1

	def generate(self):
		current_cell = self.cells[0][0]
		stack = [current_cell]
		while len(stack):
			current_cell = stack[-1]
			stack.pop()
			if self.has_neighbours(current_cell):
				stack.append(current_cell)
			print(len(stack))
			index = self.get_random_neighbour(current_cell)
			if index != -1:
				self.visit_cell(current_cell.x, current_cell.y, self.moves[index])
				stack.append(self.cells[current_cell.x + self.moves[index][0]][current_cell.y + self.moves[index][1]])
			for i in range(self.columns):
				for j in range(self.rows):
					print(self.cells[i][j], end=' || ')
				print(" ")
				print("----------------------------------------------------")


		"""
		for i in self.cells:
			for j in i:
				for k in range(4):
					if j.walls[k]:
						print(k, end=' ')
					else:
						print("_", end=' ')
				print(" || ", end=' ')
			print(" ")
			print("---------------------------------------------------------------")
		"""


class Cell:
	def __init__(self, x, y):
		# Walls: Up , Right , Bottom , Left
		self.walls = [True, True, True, True]
		self.x = x
		self.y = y
		self.visited = False

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

if __name__ == "__main__":
	maze = Maze(int(100), int(100), int(20))
	maze.generate()

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

