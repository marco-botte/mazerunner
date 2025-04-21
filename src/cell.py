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

    def draw_to(self, cell: "Cell", undo=False) -> None:
        inbetween_centers = (
            Point(self.center.x, cell.center.y)
            if self.center.x < cell.center.x
            else Point(cell.center.x, self.center.y)
        )
        line_1 = Line(self.center, inbetween_centers)
        line_2 = Line(inbetween_centers, cell.center)
        color = "gray" if undo else "red"
        self._window.draw_line(line_1, color)
        self._window.draw_line(line_2, color)

    def draw(self) -> None:
        if self.has_top_wall:
            line = Line(self._top_left, self._top_right)
            self._window.draw_line(line, "white")
        if self.has_left_wall:
            line = Line(self._top_left, self._bottom_left)
            self._window.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(self._bottom_left, self._bottom_right)
            self._window.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(self._bottom_right, self._top_right)
            self._window.draw_line(line, "white")

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

    @cached_property
    def center(self) -> Point:
        return Point(
            (self._top_left.x + self._bottom_right.x) / 2,
            (self._top_left.y + self._bottom_right.y) / 2,
        )
