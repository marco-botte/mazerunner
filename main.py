from src.line import Line, Point
from src.window import Window


def main() -> None:
    p1 = Point(100, 100)
    p2 = Point(200, 200)
    line = Line(p1, p2)
    p3 = Point(100, 200)
    p4 = Point(200, 300)
    line2 = Line(p3, p4)
    win = Window(800, 600)
    win.draw_line(line, "red")
    win.draw_line(line2, "blue")
    win.wait_for_close()


if __name__ == "__main__":
    main()
