import pygame
from Player import *
from Screen import *
from Menu import *
from CoinGenerator import *
from Scoreboard import *
from Timer import *
import Color as color


class Game:
    def __init__(self):
        self.screen = Screen(500 + 1, 320 + 1, color.black, "Maze Game")
        self.fps = 60
        self.running = True
        self.clock = pygame.time.Clock()
        self.difficulty = 0
        self.scoreboard = Scoreboard()
        self.menu = Menu(self.scoreboard.get_highest_score())
        pygame.init()

    def pressed_exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

    def quit(self):
        self.running = False

    def choose_difficulty(self):
        self.difficulty = 1 # Remove
        return
        while self.difficulty == 0 and self.running:
            self.clock.tick(self.fps)
            difficulty = self.screen.draw_menu(self.menu)
            if difficulty:
                self.difficulty = difficulty
            self.pressed_exit()

    def set_difficulty(self):
        if self.difficulty == 1:
            return (500, 500, 100, 50)
        elif self.difficulty == 2:
            return (500, 500, 50, 30)
        elif self.difficulty == 3:
            return 500, 500, 35, 20
        else:
            exit()


    def update_score(self, player, coin, score, high_score, coin_generator):
        if player.picked_coin(coin):
            coin = coin_generator.generate_coin()
            multiplier = 2 + (self.difficulty == 2) * 3 + (self.difficulty == 3) * 10
            score += 1 * multiplier
            if score > high_score:
                self.scoreboard.set_highest_score(score)
                high_score = score
            return coin, score, high_score
        else:
            return coin, score, high_score

    def start(self):
        width, height, cell_size, player_size = self.set_difficulty()
        self.screen = Screen(width + 1, height + 50 + 1, color.black, "Maze Game")
        maze = Maze(width, height, cell_size)
        maze.generate()
        coin_generator = CoinGenerator((maze.columns, maze.rows), cell_size)
        coin = coin_generator.generate_coin()
        player = Player(Point(0, 0), player_size, color.green, 5, 50)
        score = 0
        highest_score = self.scoreboard.get_highest_score()
        timer = Timer()
        timer.start()
        n = 60
        while self.running and timer.get_seconds() < n:
            self.clock.tick(self.fps)
            coin, score, highest_score = self.update_score(player, coin, score, highest_score, coin_generator)
            self.pressed_exit()
            player.move(maze)
            self.screen.refresh(maze, player, coin, (score, highest_score), n - timer.get_seconds())
        self.screen.draw_game_over()
        self.update_score(player, coin, score, highest_score, coin_generator)
        self.reset_game()

    def reset_game(self):
        self.screen = Screen(500 + 1, 320 + 1, color.black, "Maze Game")
        self.running = True
        self.difficulty = 0
        self.menu.set_highest_score(self.scoreboard.get_highest_score())
        self.choose_difficulty()
        self.start()



