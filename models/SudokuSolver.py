from typing import Dict, Tuple

from models.Variable import Variable


class SudokuSolver:
    MAX_DIMENSION = 9
    def __init__(self, sudoku: List[List[int]]):
        self.variables = self.__generate_variables()

    def __get_or_create_variable(self, coordinate: Tuple[int, int]):
        if coordinate not in self.variables:
            self.variables[coordinate] = Variable(coordinate, list(range(self.MAX_DIMENSION)))

    def __generate_variables(self, sudoku) -> Dict[Tuple[int, int], Variable]:
        result = [self.__get_or_create_variable(())]

