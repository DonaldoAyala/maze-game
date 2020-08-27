from random import randint
import Color as color

class Coin:

	def __init__(self, center, radius):
		self.center = center
		self.radius = radius
	
	def __str__(self):
		return "(" + str(self.center[0]) + ", " + str(self.center[1]) + ") r:" + str(self.radius) 
	

class CoinGenerator:

	def __init__(self, maze_dimensions, cell_size):
		self.is_coin = False
		self.maze_dimensions = maze_dimensions
		self.cell_size = cell_size

	def generate_coin(self) -> Coin:
		pos_x = self.cell_size * randint(0,self.maze_dimensions[0] - 1) + (self.cell_size // 2)
		pos_y = self.cell_size * randint(0,self.maze_dimensions[1] - 1) + self.cell_size // 2
		return Coin( (pos_x, pos_y), self.cell_size // 4)

cg = CoinGenerator((5,5), 100)
coin = cg.generate_coin()
print(coin)