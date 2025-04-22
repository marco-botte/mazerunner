import arcade

from src.config import Config
from src.window import Window


def main() -> None:
    cfg = Config(width=1000, fps=60, n_rows=30, n_cols=30)
    Window(cfg)
    arcade.run()


if __name__ == "__main__":
    main()
