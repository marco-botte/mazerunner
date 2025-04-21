import random

from .cell import Cell
from .point import Point


class Maze:
    def __init__(self, num_rows: int, num_cols: int, cell_width: int, cell_height: int) -> None:
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.random = random.Random(num_rows)
        self.cells = self._create_cells()
        self._break_walls(0, 0)

    @classmethod
    def from_dimensions(cls, width: int, height: int, num_rows: int, num_cols: int) -> "Maze":
        cell_width = round(width / (num_rows + 4))  # 2 padding on each side
        cell_height = round(height / (num_cols + 4))  # 2 padding on each side
        return cls(num_rows, num_cols, cell_width, cell_height)

    def cell(self, i: int, j: int) -> Cell:
        return self.cells[i][j]

    def _create_cells(self) -> list[list[Cell]]:
        cells: list[list[Cell]] = []
        for idx_x in range(self.num_rows):
            new_row: list[Cell] = []
            for idx_y in range(self.num_cols):
                left = 2 * self.cell_width + idx_x * self.cell_width
                right = left + self.cell_width
                top = 2 * self.cell_height + idx_y * self.cell_height
                bottom = top + self.cell_height
                new_row.append(Cell(Point(left, top), Point(right, bottom)))
            cells.append(new_row)
        cells[0][0].remove_wall("top")
        cells[-1][-1].remove_wall("bottom")
        return cells

    def _break_walls(self, x_idx: int, y_idx: int) -> None:
        cell = self.cells[x_idx][y_idx]
        cell.visited = True
        while True:
            possible = [
                cell
                for cell in self._adjacent_to(x_idx, y_idx)
                if not self.cells[cell[0]][cell[1]].visited
            ]
            if not possible:
                break
            next_x, next_y, direction = self.random.choice(possible)
            cell.remove_wall(direction)
            self.cells[next_x][next_y].remove_wall(direction, True)
            self._break_walls(next_x, next_y)

    def _adjacent_to(self, x_idx: int, y_idx: int) -> list[tuple[int, int, str]]:
        left = (x_idx - 1, y_idx, "left")
        right = (x_idx + 1, y_idx, "right")
        top = (x_idx, y_idx - 1, "top")
        bottom = (x_idx, y_idx + 1, "bottom")
        return [
            adj
            for adj in [left, right, top, bottom]
            if 0 <= adj[0] < self.num_rows and 0 <= adj[1] < self.num_cols
        ]
