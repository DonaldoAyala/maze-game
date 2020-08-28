from os.path import exists
from os.path import isfile

class Scoreboard:

	def __init__(self):
		self.local_score = 0
		self.highest_score = self.get_highest_score()

	def get_highest_score(self):
		if exists("./files/highest_score.txt") and isfile("./files/highest_score.txt"):
			with open("./files/highest_score.txt", "r") as file:
				return int(file.read())
		else:
			with open("./files/highest_score.txt", "w") as file:
				file.write("0")
			return 0

	def set_highest_score(self, new_score):
		with open("./files/highest_score.txt", "w") as file:
			file.write(str(new_score))
