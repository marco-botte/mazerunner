import random

from .cell import Cell, Direction
from .config import Config
from .point import Point


class Maze:
    def __init__(self, num_rows: int, num_cols: int, cell_width: int, cell_height: int) -> None:
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.cells = self._create_cells()
        self._break_walls(0, 0)

    @classmethod
    def from_config(cls, cfg: Config) -> "Maze":
        # 2 padding units to each border
        cell_width = round(cfg.width / (cfg.n_rows + 4))
        cell_height = round(cfg.height / (cfg.n_cols + 4))
        return cls(cfg.n_rows, cfg.n_cols, cell_width, cell_height)

    def cell(self, i: int, j: int) -> Cell:
        return self.cells[i][j]

    def _create_cells(self) -> list[list[Cell]]:
        cells: list[list[Cell]] = []
        x_base = 2 * self.cell_width
        y_base = 2 * self.cell_height
        for idx_x in range(self.num_rows):
            new_row: list[Cell] = []
            for idx_y in range(self.num_cols):
                left = x_base + idx_x * self.cell_width
                right = left + self.cell_width
                top = y_base + idx_y * self.cell_height
                bottom = top + self.cell_height
                new_row.append(Cell(Point(left, top), Point(right, bottom)))
            cells.append(new_row)
        return cells

    def _break_walls(self, x: int, y: int) -> None:
        cell = self.cells[x][y]
        cell.visited = True
        while True:
            unvisited = [c for c in self._adjacent_to(x, y) if not self.cells[c[0]][c[1]].visited]
            if not unvisited:
                break
            next_x, next_y, direction = random.choice(unvisited)
            cell.remove_wall(direction)
            self.cells[next_x][next_y].remove_wall(direction, True)
            self._break_walls(next_x, next_y)

    def _adjacent_to(self, x_idx: int, y_idx: int) -> list[tuple[int, int, Direction]]:
        left = (x_idx - 1, y_idx, Direction.LEFT)
        right = (x_idx + 1, y_idx, Direction.RIGHT)
        top = (x_idx, y_idx - 1, Direction.TOP)
        bottom = (x_idx, y_idx + 1, Direction.BOTTOM)
        in_bounds = lambda pt: 0 <= pt[0] < self.num_rows and 0 <= pt[1] < self.num_cols  # noqa: E731
        return [adj for adj in [left, right, top, bottom] if in_bounds(adj)]
