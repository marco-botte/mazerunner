from dataclasses import dataclass


@dataclass
class Config:
    n_cols: int
    width: int = 1000

    @property
    def height(self) -> int:
        return (self.width * 3) // 4

    @property
    def n_rows(self) -> int:
        return self.n_cols

    @property
    def fps(self) -> int:
        return self.n_cols * 2  # tinker with this or get user input
