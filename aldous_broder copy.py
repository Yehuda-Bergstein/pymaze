from __future__ import absolute_import
from src.maze_manager import MazeManager
from src.maze import Maze
import logging
import random
import matplotlib

# Set the logging level of matplotlib to WARNING to hide DEBUG and INFO messages
logging.getLogger('matplotlib').setLevel(logging.WARNING)


if __name__ == "__main__":

    # create a maze manager to handle all operations
    manager = MazeManager()
    walls = {'top': False, 'right': False, 'bottom': False, 'left': False}

    # now create a maze using the binary tree method
    

    # add this maze to the maze manager
   

    def find_cell_with_walls(maze, walls):
        add=0
        for row in maze.grid:
            for cell in row:
                print(cell.walls)
                print("row: " + str(cell.row) + " col: " + str(cell.col))
                if not cell.walls == walls :
                    add= add+1
                    loc = "row: " + str(cell.row) + " col: " + str(cell.col)
                    # Print the coordinates of the current cell
                   
        print(add)
        if add == 7*9:
            
            maze = manager.add_existing_maze(maze)
            manager.show_maze(maze.id)


    # show the maze
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 7)
    maze_using_aldous_broder = Maze(9, 7, algorithm="aldous_broder", start_coor=(number1, number2))
    find_cell_with_walls(maze_using_aldous_broder, walls)
    
    # show how the maze was generated
    # TO DO: Fix the animation for this algorithm
