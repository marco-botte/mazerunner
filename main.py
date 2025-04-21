import arcade

from src.maze import Maze
from src.window import Window


def main() -> None:
    width = 1000
    height = 750
    maze = Maze.from_dimensions(width, height, num_rows=20, num_cols=20)
    _window = Window(width, height, maze)
    arcade.run()


if __name__ == "__main__":
    main()
