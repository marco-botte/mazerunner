import arcade

from src.config import Config
from src.maze_view import MazeView


def main() -> None:
    cfg = Config(n_cols=30)
    window = arcade.Window(
        cfg.width, cfg.height, "mazerunner", update_rate=1 / cfg.fps, draw_rate=1 / cfg.fps
    )
    window.show_view(MazeView(cfg))
    arcade.run()


if __name__ == "__main__":
    main()
