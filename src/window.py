import signal

import arcade
import arcade.clock

from .maze import Maze
from .renderer import BACKGROUND_COLOR, Renderer

SECS_UNTIL_START = 2
SECS_UNTIL_CLOSING = 3


class Window(arcade.Window):
    def __init__(self, width: int, height: int, maze: Maze, fps: int) -> None:
        super().__init__(width, height, "mazerunner", update_rate=1 / fps, draw_rate=1 / fps)
        arcade.set_background_color(BACKGROUND_COLOR)
        self.renderer = Renderer(maze, scale=width / 5000)
        self.path_length = 0
        self.clock = arcade.clock.Clock()
        self.finished = 0.0

    def on_update(self, delta_time: float) -> None:
        self.clock.tick(delta_time)
        if self.clock.time > SECS_UNTIL_START:
            self.path_length += 1
        if self.renderer.solved_maze and not self.finished:
            self.finished = self.clock.time
        if self.finished and self.clock.time_since(self.finished) > SECS_UNTIL_CLOSING:
            self.on_close()

    def on_close(self) -> None:
        signal.raise_signal(signal.SIGINT)

    def on_draw(self) -> None:
        self.renderer.draw(self.path_length)
