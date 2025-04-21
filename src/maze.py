import time

from .cell import Cell
from .line import Point
from .window import Window


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        window: Window,
    ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self._cells = self._create_cells()
        self._draw_cells()

    def _create_cells(self) -> list[list[Cell]]:
        cells: list[list[Cell]] = []
        for idx_x in range(self.num_rows):
            new_row: list[Cell] = []
            for idx_y in range(self.num_cols):
                left = self.x1 + idx_x * self.cell_size_x
                right = left + self.cell_size_x
                top = self.y1 + idx_y * self.cell_size_y
                bottom = top + self.cell_size_y
                new_row.append(Cell(Point(left, top), Point(right, bottom), self.window))
            cells.append(new_row)
        cells[0][0].remove_wall("top")
        cells[-1][-1].remove_wall("bottom")
        return cells

    def _draw_cells(self) -> None:
        for cell_row in self._cells:
            for cell in cell_row:
                cell.draw()

    def _animate(self) -> None:
        self.window.redraw()
        time.sleep(0.05)
