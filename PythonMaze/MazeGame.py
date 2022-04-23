from Game import *

if __name__ == "__main__":
    # 500 500 100 , 50
    # 500 500 50 , 30
    # 500 500 35 , 20
    game = Game()
    game.choose_difficulty()
    game.start()
    pygame.quit()