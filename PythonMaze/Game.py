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
        self.action = 0
        self.scoreboard = Scoreboard()
        self.menu = Menu(self.scoreboard.get_best_score())
        pygame.init()

    def pressed_exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

    def quit(self):
        self.running = False

    def wait_action(self):
        while self.action == 0 and self.running:
            self.clock.tick(self.fps)
            action = self.screen.draw_menu(self.menu)
            if action == 1:
                self.action = action
            elif action == -1:
                self.quit()
            self.pressed_exit()

    def get_dimensions(self):
        return 500, 500, 35, 20

    def update_score(self, new_score):
        best_score = self.scoreboard.get_best_score()
        if best_score != -1:
            if new_score < best_score:
                self.scoreboard.set_best_score(new_score)

    def start(self):
        width, height, cell_size, player_size = self.get_dimensions()
        self.screen = Screen(width + 1, height + 50 + 1, color.black, "Maze Game")
        maze = Maze(width, height, cell_size)
        maze.generate()
        player = Player(Point(0, 0), player_size, color.green, 5, 50)
        best_score = self.scoreboard.get_best_score()
        timer = Timer()
        timer.start()
        time_elapsed = 0
        while self.running:
            self.clock.tick(self.fps)
            self.pressed_exit()
            player.move(maze)
            time_elapsed = timer.get_seconds()
            self.screen.refresh(maze, player, (time_elapsed, best_score), time_elapsed)
        self.update_score(time_elapsed)
        self.screen.draw_game_over()
        self.reset_game()

    def reset_game(self):
        self.screen = Screen(500 + 1, 320 + 1, color.black, "Maze Game")
        self.running = True
        self.action = 0
        self.menu.set_best_score(self.scoreboard.get_best_score())
        self.wait_action()
        if self.running and self.start_game == 1:
            self.start()



