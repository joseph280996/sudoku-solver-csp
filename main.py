import argparse

from services import json_file_parser_service
from models import SudokuSolver

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--data", default="data.json", help="The path to boxes JSON file for testing")

if __name__ == '__main__':
    args = parser.parse_args()
    file_data = getattr(args, 'data')
    sudoku = json_file_parser_service.parse(file_data)

    solver = SudokuSolver(sudoku)
    solver.solve()
    solver.display()
