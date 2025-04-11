from graphics import Window
from maze import Maze
import sys

def main():
    num_rows = 12
    num_columns = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x -2 * margin) / num_columns
    cell_size_y = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_columns, cell_size_x, cell_size_y, win, 10)
    print("maze created")
    is_solvable = maze.solve()
    if not is_solvable:
        print("maze can not be solved")
    else:
        print("maze solve!!")

    win.wait_for_close()


main()
