from tkinter import BOTH, Canvas, Tk

from .line import Line


class Window:
    def __init__(self, width: int, height: int) -> None:
        self.root = Tk()
        self.root.title("Window")
        self.root.geometry(f"{width}x{height}")
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=True)
        self.width = width
        self.height = height
        self.running = False

    def wait_for_close(self) -> None:
        self.running = True
        while self.running:
            self.redraw()

    def close(self) -> None:
        self.root = Tk()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.root.update()
        self.root.update_idletasks()

    def draw_line(self, line: Line, fill_color: str) -> None:
        line.draw(self.canvas, fill_color)
