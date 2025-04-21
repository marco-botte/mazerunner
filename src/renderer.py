from typing import Sequence

import arcade

from .cell import Cell
from .maze import Maze
from .point import Point

BACKGROUND_COLOR = arcade.color.CADET_BLUE
DRAW_COLOR = arcade.color.ASH_GREY
HIGHLIGHT_COLOR = arcade.color.FRENCH_WINE  # ac1e44 for icons

START = arcade.Sprite("assets/icons/start.png", 0.2, hit_box_algorithm="None")
FINISH = arcade.Sprite("assets/icons/finish.png", 0.2, hit_box_algorithm="None")


class Renderer:
    def __init__(self, maze: Maze):
        self.maze = maze
        self.start = START
        self.finish = FINISH
        self.start.position = (maze.cells[0][0].center.x, maze.cells[0][0].center.y)
        self.finish.position = (maze.cells[-1][-1].center.x, maze.cells[-1][-1].center.y)

    def draw(self) -> None:
        self._draw_cells()
        self._draw_border()
        self._draw_sprites([self.start, self.finish])

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
            self._draw_line(line_start, line_end, color=HIGHLIGHT_COLOR)

    def _draw_cell(self, cell: Cell, color: arcade.color.Color = DRAW_COLOR) -> None:
        for line in cell.wall_lines:
            self._draw_line(line[0], line[1], color)

    def _draw_line(self, a: Point, b: Point, color: arcade.color.Color = DRAW_COLOR) -> None:
        arcade.draw_line(a.x, a.y, b.x, b.y, color, line_width=2)

    def _draw_sprites(self, sprites: Sequence[arcade.Sprite]) -> None:
        sl: arcade.SpriteList = arcade.SpriteList()
        sl.extend(sprites)
        sl.draw()
        sl.clear()
