from src.cell import Cell
from src.line import Point
from src.window import Window


def main() -> None:
    p1 = Point(100, 100)
    p2 = Point(200, 200)
    p3 = Point(100, 200)
    p4 = Point(200, 300)
    window = Window(800, 600)
    cell_1 = Cell(p1, p2, window)
    cell_2 = Cell(p3, p4, window)
    cell_1.draw()
    cell_2.draw()
    cell_1.draw_to(cell_2)
    cell_2.draw_to(cell_1)
    window.wait_for_close()


if __name__ == "__main__":
    main()
