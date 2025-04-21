from dataclasses import dataclass
from tkinter import Canvas


@dataclass
class Point:
    x: float
    y: float


class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2
        )
