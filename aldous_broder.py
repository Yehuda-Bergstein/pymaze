from __future__ import absolute_import
from src.maze_manager import MazeManager
from src.maze import Maze


if __name__ == "__main__":

    # create a maze manager to handle all operations
    manager = MazeManager()

    # now create a maze using the binary tree method
    maze_using_aldous_broder = Maze(9, 7, algorithm="aldous_broder",start_coor=(1,1))

    # add this maze to the maze manager
    maze_using_aldous_broder = manager.add_existing_maze(maze_using_aldous_broder)
    walls= {'top': False, 'right': True, 'bottom': True, 'left': True}
    # Add more wall configurations as needed

    def find_cell_with_walls(maze_using_aldous_broder,walls):
        for row in maze_using_aldous_broder.grid:
            for cell in row:  # Add this line
                print(cell.walls)
                print("row: "+str(cell.row) + " col: " + str(cell.col))
                if cell.walls == walls:
                    loc = "row: "+str(cell.row) + " col: " + str(cell.col)
                      # Print the coordinates of the current cell
                    return True, loc
                
                
        return False


    # show the maze
    manager.show_maze(maze_using_aldous_broder.id)
    print(find_cell_with_walls(maze_using_aldous_broder,walls))




    # show how the maze was generated
    # TO DO: Fix the animation for this algorithm