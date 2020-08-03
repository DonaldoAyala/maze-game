import pygame

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
		pygame.init()
		run = True
		while run:
			pygame.time.delay(20)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
			self.screen.window.fill((COLORS["BLACK"]))
			self.screen.draw_maze("hello")


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
	def __init__(self, screen_width, screen_height, cell_size):
		self.columns = screen_width / cell_size
		self.rows = screen_height / cell_size
		self.cells = [[Cell(0, 0)]*self.columns for i in range(self.rows)]
		for i in range(self.columns):
			for j in range(self.rows):
				self.cells[i][j].x = i * cell_size
				self.cells[i][j].y = j * cell_size

	def visit_cell(self, x, y, move):
		if x + move[0] < 0 or x + move[1] >= self.columns:
			return False
		if y + move[1] < 0 or y + move[1] >= self.rows:
			return False
		if self.cells[x + move[0]][y + move[1]].visited:
			return False
		top = [0, -1]
		right = [1, 0]
		bottom = [0, 1]
		left = [-1, 0]
		if move == top:
			self.cells[x][y].remove_wall(0) # Top
			self.cells[x + move[0]][y + move[1]].remove_wall(2) # Bottom
		elif move == right:
			self.cells[x][y].remove_wall(1) # Right
			self.cells[x + move[0]][y + move[1]].remove_wall(3) # Left
		elif move == bottom:
			self.cells[x][y].remove_wall(2) # Bottom
			self.cells[x + move[0]][y + move[1]].remove_wall(0) # Top
		else:
			self.cells[x][y].remove_wall(3) # Left
			self.cells[x + move[0]][y + move[1]].remove_wall(1) # Right
		return True

	def generate(self):
		current_cell = self.cells[0][0]
		stack = []
		# Moves are: top right bottom left
		moves = [[0, -1], [1, 0], [0, 1], [-1, 0]]
		stack.append(current_cell)
		while  not stack.empty():
			current_cell = stack.top()
			stack.pop()
			for mvs in moves:
				if self.visit_cell(current_cell.x, current_cell.y, mvs):
					stack.append(self.cells[current_cell.x + mvs[0]][current_cell.y + mvs[1]])
					self.cells[current_cell.x + mvs[0]][current_cell.y + mvs[1]].visited = True


class Cell:
	def __init__(self, x, y):
		# Walls: Up , Right , Bottom , Left
		self.walls = {True, True, True, True}
		self.x = x
		self.y = y
		self.visited = False

	def remove_wall(self, wall):
		self.walls[wall] = False


if __name__ == "__main__":
	game = Game()
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

