import pygame

COLORS = {
	"WHITE" : (255,255,255),
	"BLACK" : (0,0,0),
	"RED" 	: (255,0,0),
	"GREEN" : (0,255,0),
	"BLUE"	: (0,0,255)
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
		pygame.draw.rect(self.window, COLORS["GREEN"], (10, 10, 10, 10))
		pygame.display.update()

class Maze:
	def __init__(self, screenWidth, screenHeight, cellSize):
		self.width = screenWidth / cellSize
		self.height = screenHeight / cellSize
		self.cells = [[Cell()]*self.width  for i in range(self.height)]

class Cell:
	def __init__(self):
		# Walls: Up , Right , Bottom , Left
		self.walls = {True , True , True , True}
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

