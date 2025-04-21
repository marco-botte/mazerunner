from functools import cached_property

from .line import Line, Point
from .window import Window

CELL_WALLS = {
    "top": "has_top_wall",
    "left": "has_left_wall",
    "bottom": "has_bottom_wall",
    "right": "has_right_wall",
}


class Cell:
    def __init__(self, top_left: Point, bottom_right: Point, window: Window) -> None:
        self._top_left = top_left
        self._bottom_right = bottom_right
        self._window = window
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self) -> None:
        if self.has_top_wall:
            line = Line(self._top_left, self._top_right)
            self._window.draw_line(line, "red")
        if self.has_left_wall:
            line = Line(self._top_left, self._bottom_left)
            self._window.draw_line(line, "red")
        if self.has_bottom_wall:
            line = Line(self._bottom_left, self._bottom_right)
            self._window.draw_line(line, "red")
        if self.has_right_wall:
            line = Line(self._bottom_right, self._top_right)
            self._window.draw_line(line, "red")

    def remove_wall(self, direction: str) -> None:
        if direction not in CELL_WALLS:
            return
        setattr(self, CELL_WALLS[direction], False)

    @cached_property
    def _top_right(self) -> Point:
        return Point(self._bottom_right.x, self._top_left.y)

    @cached_property
    def _bottom_left(self) -> Point:
        return Point(self._top_left.x, self._bottom_right.y)
