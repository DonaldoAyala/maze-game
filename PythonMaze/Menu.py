import pygame
import random
import Color as color


class Menu:
	def __init__(self):
		self.buttons = []
		# 'Easy difficulty button'
		self.buttons.append(Button((50,300),(100,30),(color.gray),"Easy"))
		# 'Medium difficulty button'
		self.buttons.append(Button((200,300),(100,30),(color.gray),"Medium"))
		# 'Hard difficulty button'
		self.buttons.append(Button((350,300),(100,30),(color.gray),"Hard"))

class Button:

	def __init__(self, position, size, color, text):
		self.position = position
		self.size = size
		self.color = color
		self.text = text

	def change_color(self, color):
		self.color = color

	def clicked_over(self, clicked_pos):
		if self.position[0] < clicked_pos[0] < self.position[0] + self.size[0] \
				and self.position[1] < clicked_pos[1] < self.position[1] + self.size[1]:
			return True
		else:
			return False