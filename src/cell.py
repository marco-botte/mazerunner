from functools import cached_property

from .point import Point

CELL_WALLS = {
    "top": "has_top_wall",
    "left": "has_left_wall",
    "bottom": "has_bottom_wall",
    "right": "has_right_wall",
}


class Cell:
    def __init__(self, top_left: Point, bottom_right: Point) -> None:
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

    def remove_wall(self, direction: str, opposite: bool = False) -> None:
        if direction not in CELL_WALLS:
            return
        if not opposite:
            setattr(self, CELL_WALLS[direction], False)
            return
        if direction == "right":
            setattr(self, CELL_WALLS["left"], False)
        if direction == "left":
            setattr(self, CELL_WALLS["right"], False)
        if direction == "top":
            setattr(self, CELL_WALLS["bottom"], False)
        if direction == "bottom":
            setattr(self, CELL_WALLS["top"], False)

    @cached_property
    def top_right(self) -> Point:
        return Point(self.bottom_right.x, self.top_left.y)

    @cached_property
    def bottom_left(self) -> Point:
        return Point(self.top_left.x, self.bottom_right.y)

    @cached_property
    def center(self) -> Point:
        return Point(
            (self.top_left.x + self.bottom_right.x) / 2,
            (self.top_left.y + self.bottom_right.y) / 2,
        )

    @property
    def wall_lines(self) -> list[tuple[Point, Point]]:
        lines: list[tuple[Point, Point]] = []
        if self.has_top_wall:
            lines.append((self.top_left, self.top_right))
        if self.has_left_wall:
            lines.append((self.top_left, self.bottom_left))
        if self.has_bottom_wall:
            lines.append((self.bottom_left, self.bottom_right))
        if self.has_right_wall:
            lines.append((self.bottom_right, self.top_right))
        return lines
