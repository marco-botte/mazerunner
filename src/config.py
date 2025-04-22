from dataclasses import dataclass


@dataclass
class Config:
    width: int
    fps: int
    n_rows: int
    n_cols: int

    @property
    def height(self) -> int:
        return (self.width * 3) // 4
