from functools import cached_property
from itertools import pairwise

import arcade

from .cell import Cell
from .maze import Maze
from .maze_runner import MazeRunner
from .point import Point

BACKGROUND_COLOR = arcade.color.CADET_BLUE
WALL_COLOR = arcade.color.ASH_GREY
HIGHLIGHT_COLOR = arcade.color.BLUEBERRY
BORDER_COLOR = arcade.color.FRENCH_WINE  # ac1e44 for icons & border
FINISH_COLOR = arcade.color.SUNGLOW


class Renderer:
    def __init__(self, maze: Maze):
        self.maze = maze
        self.runner = MazeRunner(maze)
        self.solved_maze = False
        self.border_color = BORDER_COLOR

    def draw(self, path_length: int) -> None:
        self._draw_cells()
        self._draw_border()  # border is drawn over cells in highlight color
        self._draw_icons()
        self._draw_path(path_length)

    def _draw_path(self, length: int) -> None:
        subpath = self.runner.shortest_path[:length]
        for curr, next in pairwise(subpath):
            cell = self.maze.cell(*curr)
            next_cell = self.maze.cell(*next)
            self._draw_line(cell.center, next_cell.center, HIGHLIGHT_COLOR)
        if length >= len(self.runner.shortest_path):
            self.solved_maze = True
            self.border_color = FINISH_COLOR

    def _draw_cells(self) -> None:
        for cell_row in self.maze.cells:
            for cell in cell_row:
                self._draw_cell(cell)

    def _draw_border(self) -> None:
        left = (self.maze.cells[0][0].top_left, self.maze.cells[0][-1].bottom_left)
        bottom = (self.maze.cells[0][-1].bottom_left, self.maze.cells[-1][-1].bottom_right)
        right = (self.maze.cells[-1][-1].bottom_right, self.maze.cells[-1][0].top_right)
        top = (self.maze.cells[-1][0].top_right, self.maze.cells[0][0].top_left)
        for line_start, line_end in [left, bottom, right, top]:
            self._draw_line(line_start, line_end, color=self.border_color)

    def _draw_cell(self, cell: Cell, color: arcade.color.Color = WALL_COLOR) -> None:
        for line in cell.wall_lines:
            self._draw_line(line[0], line[1], color)

    def _draw_line(self, a: Point, b: Point, color: arcade.color.Color = WALL_COLOR) -> None:
        arcade.draw_line(a.x, a.y, b.x, b.y, color, line_width=2)

    def _draw_icons(self) -> None:
        sl: arcade.SpriteList = arcade.SpriteList()
        sl.extend([self.start, self.finish])
        sl.draw()
        sl.clear()  # avoids memory leak

    @cached_property
    def start(self) -> arcade.Sprite:
        start = arcade.Sprite("assets/icons/start.png", 0.2, hit_box_algorithm="None")
        start.position = (self.maze.cells[0][0].center.x, self.maze.cells[0][0].center.y)
        return start

    @cached_property
    def finish(self) -> arcade.Sprite:
        finish = arcade.Sprite("assets/icons/finish.png", 0.2, hit_box_algorithm="None")
        finish.position = (self.maze.cells[-1][-1].center.x, self.maze.cells[-1][-1].center.y)
        return finish
