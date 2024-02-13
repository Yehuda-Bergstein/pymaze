from __future__ import absolute_import
from src.maze_manager import MazeManager
from src.maze import Maze


if __name__ == "__main__":

    # create a maze manager to handle all operations
    manager = MazeManager()

    # now create a maze using the binary tree method
    maze = Maze(9, 7, algorithm="dfs_backtrack",start_coor=(0,0))

    # add this maze to the maze manager
    maze= manager.add_existing_maze(maze)

    # show the maze
    manager.show_maze(maze.id)
    # show how the maze was generated
    # TO DO: Fix the animation for this algorithm

    manager.solve_maze(maze.id, "DepthFirstBacktracker")

    manager.show_solution_animation(maze.id)
    manager.show_generation_animation(maze.id)




