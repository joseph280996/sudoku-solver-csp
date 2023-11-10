from typing import Any, Tuple, Generator


class SudokuSubgridVisitor: 
    MAX_COUNT = 9
    def __init__(self, coordinate: Tuple[int, int]):
        self.coordinate = coordinate
        self.count = 0

    def has_next(self) -> bool:
        return self.count < self.MAX_COUNT

    def next(self) -> Generator[Tuple[int, int], Any, Any]:
        row_index, col_index = self.coordinate
        row_start_index = row_index // 3 * 3
        col_start_index = col_index // 3 * 3

        for row in range(row_start_index, row_start_index + 1):
            for col in range(col_start_index, col_start_index + 1):
                yield (row,col)
                self.count += 1

