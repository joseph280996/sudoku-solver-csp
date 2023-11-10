from typing import Tuple, List, cast

from models import Variable, SudokuSubgridVisitor


class SudokuSolver:
    MAX_DIMENSION = 9
    def __init__(self, sudoku: List[List[int]]):
        self.variables = {}
        self.__create_all_variables(sudoku)

    def __get_or_create_variable(self, coordinate: Tuple[int, int]) -> Variable:
        if coordinate not in self.variables:
            self.variables[coordinate] = Variable(coordinate, list(range(self.MAX_DIMENSION)))
        return self.variables[coordinate]
    
    def __create_all_variables(self, sudoku) -> None:
        assigned_variables: List[Tuple[int, int, int]] = []
        for i in range(len(sudoku)) :
            for j in range(len(sudoku)):
                if sudoku[i][j] is None:
                    var = self.__get_or_create_variable((i, j))
                    var.constraints = self.__generate_constraints((i, j))
                else:
                    assigned_variables.append((i, j, sudoku[i][j]))

        for i, j, val in assigned_variables:
            var = self.variables[(i, j)]
            del self.variables[(i,j)]
            for constraints_var in var.constraints:
                constraints_var.domain.remove(val)


    def __generate_constraints(self, coordinate:Tuple[int, int]) -> List[Variable]:
        # Up
        result = [self.__get_or_create_variable((coordinate[0], i)) for i in range(coordinate[0], self.MAX_DIMENSION)]

        # Down
        result = result + [self.__get_or_create_variable((coordinate[0], i)) for i in range(0, coordinate[0])]

        # Left
        result = result + [self.__get_or_create_variable((i,coordinate[1])) for i in range(0, coordinate[1])]

        # Right
        result = result + [self.__get_or_create_variable((i,coordinate[1])) for i in range(coordinate[1], self.MAX_DIMENSION)]

        # 3x3 traverse
        visitor = SudokuSubgridVisitor(coordinate)
        while visitor.has_next():
            next_coord = cast(Tuple[int, int], visitor.next())
            result.append(self.__get_or_create_variable(next_coord))

        return result

