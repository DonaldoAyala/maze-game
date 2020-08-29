# Lucky Maze

> ### Menu preview
> ![menu](https://github.com/DonaldoAyala/Maze_Game/blob/master/.images/menu.png)
> ### In-Game preview
> ![in_game](https://github.com/DonaldoAyala/Maze_Game/blob/master/.images/in_game.png)


## Description

> Lucky Maze is a game which generates a random maze as well as coins around the maze.

> The game has 3 difficulties (Easy, Medium and Hard) and each difficulty has a coin multiplier (x2 for Easy,  x5 for Medium and x12 for Hard).


## Objective

> The goal of the game is to gather as many coins as you can in 60 seconds.


## Developement
* The maze generation begins with a grid full of walls, and then the *bfs* algorithm follows which removes the walls as it goes on.

* The maze is generated using a [randomized breadth first search algorithm](https://en.wikipedia.org/wiki/Maze_generation_algorithm#Randomized_depth-first_search). 

* Programmed with Python's module [Pygame](https://www.pygame.org/wiki/about)

## How to play
1) In order to play ***Lucky Maze***  you need to install pygame. See more [here](https://www.pygame.org/wiki/GettingStarted).
2) You need to dowload the files inside the **[PythonMaze](https://github.com/DonaldoAyala/Maze_Game/tree/master/PythonMaze)** directory.
3) Open the command line, go to the location of the files and run the following command:

### First option
``` bash
 python MazeGame.py
```
### Second option
``` bash
 python3 MazeGame.py
```

