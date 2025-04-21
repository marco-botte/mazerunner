from src.maze import Maze
from src.window import Window


def main() -> None:
    window = Window(800, 600)
    _maze = Maze(
        x1=100,
        y1=100,
        num_rows=10,
        num_cols=10,
        cell_size_x=30,
        cell_size_y=30,
        window=window,
    )
    window.wait_for_close()


if __name__ == "__main__":
    main()
