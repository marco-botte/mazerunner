import signal
from dataclasses import replace

import arcade
import arcade.clock

from .config import Config
from .maze_view import MazeView
from .renderer import BACKGROUND_COLOR

NUM_RANGE = list(range(48, 57))
NUMPAD_RANGE = list(range(65456, 65465))


class ConfigView(arcade.View):
    def __init__(self, default_cfg: Config) -> None:
        super().__init__(background_color=BACKGROUND_COLOR)
        self.default_cfg = default_cfg
        self.clock = arcade.clock.Clock()
        self.raw_input = ""
        self.input = 0

    def on_close(self) -> None:
        signal.raise_signal(signal.SIGINT)

    def on_update(self, delta_time: float) -> None:
        if self.input:
            cfg = replace(self.default_cfg, n_cols=min(self.input, 40))  # rec. depth
            maze_view = MazeView(cfg)
            self.window.show_view(maze_view)

    def on_key_press(self, key: int, _modifiers: int) -> None:
        if key in NUM_RANGE:
            self.raw_input += chr(key)
        if key in NUMPAD_RANGE:
            self.raw_input += chr(key) - 65408  # offset
        if len(self.raw_input) == 2 or (key == arcade.key.ENTER and self.raw_input):
            self.input = int(self.raw_input)

    def on_draw(self):
        return super().on_draw()
