from os.path import exists
from os.path import isfile

class Scoreboard:

    def __init__(self):
        self.local_score = 0
        self.best_score = self.get_best_score()

    def get_best_score(self):
        if exists("./files/best_score.txt") and isfile("./files/best_score.txt"):
            with open("./files/best_score.txt", "r") as file:
                return int(file.read())
        else:
            with open("./files/best_score.txt", "w") as file:
                file.write("-1")
            return -1

    def set_best_score(self, new_score):
        with open("./files/best_score.txt", "w") as file:
            file.write(str(new_score))
