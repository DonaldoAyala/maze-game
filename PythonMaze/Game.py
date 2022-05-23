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
        else:
            self.scoreboard.set_best_score(new_score)

    def player_reached_exit(self):
        return 

    def start(self):
        width, height, cell_size, player_size = self.get_dimensions()
        self.screen = Screen(width + 1, height + 50 + 1, color.black, "Maze Game")
        maze = Maze(width, height, cell_size)
        maze.generate()
        player = Player(Point(0, 0), player_size, color.green, 5, 50)
        best_score = self.scoreboard.get_best_score()
        best_score = best_score if best_score != -1 else best_score
        timer = Timer()
        timer.start()
        time_elapsed = 0
        reached_exit = False
        while self.running:
            self.clock.tick(self.fps)
            self.pressed_exit()
            player.move(maze)
            time_elapsed = timer.get_seconds()
            if player.reached_exit(maze.exit_cell):
                self.running = False
                reached_exit = True
            self.screen.refresh(maze, player, best_score, time_elapsed)
        if reached_exit:
            self.update_score(time_elapsed)
            self.screen.draw_end_of_game()
        self.reset_game()

    def reset_game(self):
        self.screen = Screen(500 + 1, 320 + 1, color.black, "Maze Game")
        self.running = True
        self.action = 0
        self.menu.set_best_score(self.scoreboard.get_best_score())
        self.wait_action()
        if self.running and self.action == 1:
            self.start()



