import signal

import arcade

from .maze import Maze
from .maze_graph import MazeGraph
from .renderer import BACKGROUND_COLOR, Renderer


class Window(arcade.Window):
    def __init__(self, width: int, height: int, maze: Maze) -> None:
        super().__init__(width, height, "mazerunner")
        arcade.set_background_color(BACKGROUND_COLOR)
        self.maze = maze
        self.width = width
        self.height = height
        self.graph = MazeGraph(maze)
        self.renderer = Renderer(self.graph)

    def on_update(self, delta_time: float) -> None:
        super().on_update(delta_time)

    def on_close(self) -> None:
        signal.raise_signal(signal.SIGINT)

    def on_draw(self) -> None:
        self.renderer.draw()
