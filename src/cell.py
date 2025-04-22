from enum import Enum
from functools import cached_property

from .point import Point


class Direction(Enum):
    LEFT = "left"
    RIGHT = "right"
    TOP = "top"
    BOTTOM = "bottom"


def opposite(direction: Direction) -> Direction:
    match direction:
        case Direction.LEFT:
            return Direction.RIGHT
        case Direction.RIGHT:
            return Direction.LEFT
        case Direction.BOTTOM:
            return Direction.TOP
        case Direction.TOP:
            return Direction.BOTTOM
    raise ValueError("no valid direction")


class Cell:
    def __init__(self, top_left: Point, bottom_right: Point) -> None:
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

    def remove_wall(self, direction: Direction, opposite_dir: bool = False) -> None:
        dir = direction.value if not opposite_dir else opposite(direction).value
        setattr(self, f"has_{dir}_wall", False)

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
