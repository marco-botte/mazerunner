import signal
from dataclasses import replace

import arcade
import arcade.clock

from .config import Config
from .maze_view import MazeView
from .renderer import HIGHLIGHT_COLOR

NUM_RANGE = list(range(48, 57))
NUMPAD_RANGE = list(range(65456, 65465))
ANIMATION_DELAY = 1.5
MIN_MAZE_SIZE = 5
MAX_MAZE_SIZE = 25


class ConfigView(arcade.View):
    def __init__(self, default_cfg: Config) -> None:
        super().__init__()
        self.default_cfg = default_cfg
        self.clock = arcade.clock.Clock()
        self.base_color: arcade.color.Color = HIGHLIGHT_COLOR
        self.transparency = 255
        self.raw_input = ""
        self.input = 0
        self.transition = False

    def on_show_view(self):
        def initial_fade(_delta_time: float) -> None:
            self.reset_fading()

        arcade.schedule_once(initial_fade, ANIMATION_DELAY)

    def on_close(self) -> None:
        signal.raise_signal(signal.SIGINT)

    def on_update(self, delta_time: float) -> None:
        if self.input and not self.transition:
            self.transition = True
            arcade.schedule_once(self.show_maze_view, ANIMATION_DELAY)
        self.transparency = max(50, self.transparency - 2)

    def on_key_press(self, key: int, _modifiers: int) -> None:
        if key in NUM_RANGE:
            self.raw_input += chr(key)
        if key in NUMPAD_RANGE:
            self.raw_input += chr(key - 65408)  # offset
        self.reset_fading()
        if len(self.raw_input) == 2 or (key == arcade.key.ENTER and self.raw_input):
            self.input = int(self.raw_input)

    def on_draw(self):
        self.clear()
        self.text().draw()
        self.fading_text().draw()

    def show_maze_view(self, _delta_time: float) -> None:
        self.reset_fading()
        self.input = min(max(self.input, 5), MAX_MAZE_SIZE)  # rec. depth
        self.raw_input = str(self.input)

        def show(_delta_time: float) -> None:
            self.clear()
            cfg = replace(self.default_cfg, n_cols=self.input)
            maze_view = MazeView(cfg)
            self.window.show_view(maze_view)

        arcade.schedule_once(show, ANIMATION_DELAY)

    def reset_fading(self) -> None:
        self.transparency = 255

    def text(self, text: str = "") -> arcade.Text:
        sze = round(self.window.width / 15)
        x = self.window.width / 2 - 25
        y = self.window.height / 2
        return arcade.Text("x =", x, y, HIGHLIGHT_COLOR, sze, font_name="Menlo", anchor_x="right")

    def fading_text(self, text: str = "") -> arcade.Text:
        sze = round(self.window.width / 15)
        x = self.window.width / 2 + 25
        y = self.window.height / 2
        fading_color = arcade.color.Color(*self.base_color.rgb, self.transparency)
        text = self.raw_input if self.raw_input else "_"
        return arcade.Text(f"{text}", x, y, fading_color, sze, font_name="Menlo", anchor_x="left")
