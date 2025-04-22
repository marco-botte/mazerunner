import arcade

from src.config import Config
from src.config_view import ConfigView


def main() -> None:
    cfg = Config(n_cols=0)
    window = arcade.Window(cfg.width, cfg.height, update_rate=1 / 100)
    window.show_view(ConfigView(cfg))
    arcade.run()


if __name__ == "__main__":
    main()
