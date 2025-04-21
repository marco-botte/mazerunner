import arcade

from src.maze import Maze
from src.window import Window

N_ROWS = 30
N_COLS = 30
FPS = 60


def main() -> None:
    width = 1000
    height = 750
    maze = Maze.from_dimensions(width, height, num_rows=N_ROWS, num_cols=N_COLS)
    Window(width, height, maze, fps=FPS)
    arcade.run()


if __name__ == "__main__":
    main()
