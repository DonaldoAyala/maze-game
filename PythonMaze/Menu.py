import pygame
import random
import Color as color


class Menu:
	def __init__(self):
		pass


class Button:

	def __init__(self, position, size, color):
		self.position = position
		self.size = size
		self.color = color

	def change_color(self, color):
		self.color = color

	def clicked_over(self, clicked_pos):
		if self.position[0] < clicked_pos[0] < self.position[0] + self.size[0] \
				and self.position[1] < clicked_pos[1] < self.position[1] + self.size[1]:
			return True
		else:
			return False