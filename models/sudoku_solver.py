from typing import Tuple, List, Dict

from .state import State
from .backtracking import BackTrackingSearch
from .variable import Variable


class SudokuSolver:
    """
    This class represent the solver for sudoku which is a middleware with CSP class.
    Properties:
        variables: The list of Variables that was created for each cell in the sudoku grid
        csp: The CSP class instance
        solution: The solution that was found, None if not found
        MAX_DIMENSION: The dimension of the sudoku
    """

    MAX_DIMENSION = 9

    def __init__(self, sudoku: List[List[int]]):
        print("Given Problem:\n")
        self.__print_sudoku(sudoku)
        self.variables: State = self.__create_initial_state(sudoku)
        self.csp = BackTrackingSearch()
        self.solution: Dict[Tuple[int, int], int] | None = None

    def solve(self):
        """
        This function will call the search function of the CSP class to search for a solution
        """
        self.solution = self.csp.search(self.variables)

    def display(self):
        """
        This function will handle displaying the solved sudoku to the terminal
        """
        if self.solution is None:
            print("Failed to find solution to the given sudoku.")
            return

        print("Found solution:\n")

        self.__print_sudoku(
            [
                [self.solution[(row, col)] for col in range(self.MAX_DIMENSION)]
                for row in range(self.MAX_DIMENSION)
            ]
        )

    def __print_sudoku(self, sudoku: List[List[int]]):
        print("+---+---+---+  +---+---+---+  +---+---+---+")
        for idx, row in enumerate(sudoku):
            print("| {} | {} | {} |  | {} | {} | {} |  | {} | {} | {} |".format(*row))
            print("+---+---+---+  +---+---+---+  +---+---+---+")
            if idx % 3 == 2 and idx < len(sudoku) - 1:
                print("+---+---+---+  +---+---+---+  +---+---+---+")

    def __get_or_create_variable(
        self, coordinate: Tuple[int, int], state: Dict[Tuple[int, int], Variable]
    ) -> Variable:
        if coordinate not in state:
            state[coordinate] = Variable(
                coordinate, list(range(1, self.MAX_DIMENSION + 1))
            )
        return state[coordinate]

    def __create_initial_state(self, sudoku) -> State:
        state = {}

        for i in range(len(sudoku)):
            for j in range(len(sudoku)):
                if sudoku[i][j] == 0:
                    var = self.__get_or_create_variable((i, j), state)
                else:
                    var = self.__get_or_create_variable((i, j), state)
                    var.domain = [sudoku[i][j]]

                var.constraints = self.__generate_constraints((i, j))

        return State(state)

    def __generate_constraints(
        self, coordinate: Tuple[int, int]
    ) -> List[Tuple[int, int]]:
        # Down
        result = [(i, coordinate[1]) for i in range(0, coordinate[0])]

        # Up
        result = result + [
            (i, coordinate[1]) for i in range(coordinate[0] + 1, self.MAX_DIMENSION)
        ]

        # Left
        result = result + [(coordinate[0], i) for i in range(0, coordinate[1])]

        # Right
        result = result + [
            (coordinate[0], i) for i in range(coordinate[1] + 1, self.MAX_DIMENSION)
        ]

        # Create Variables for 3x3 constraints
        row_index, col_index = coordinate
        row_start_index = row_index // 3 * 3
        col_start_index = col_index // 3 * 3

        for row in range(row_start_index, row_start_index + 3):
            for col in range(col_start_index, col_start_index + 3):
                if (row, col) == coordinate or (row, col) in result:
                    continue
                result.append((row, col))

        return result
