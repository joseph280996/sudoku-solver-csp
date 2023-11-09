from typing import Dict, Tuple
from models.CSP import CSP

from models.Variable import Variable


class SudokuSolver:
    def __init__(self, sudoku: List[List[int]]):
        self.variables = {}
        self.csp = CSP(self.__generate_variables(sudoku))

    def __generate_variables(self) -> Dict[Tuple[int, int], Variable]:

