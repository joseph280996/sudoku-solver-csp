import argparse

from models.SudokuSolver import SudokuSolver

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--data", default="data.json", help="The path to boxes JSON file for testing")
test_sudoku = [
    [6, None, 8, 7, None, 2, 1, None, None],
    [4, None, None, None, 1, None, None, None, 2],
    [None, 2, 5, 4, None, None, None, None, None],
    [7, None, 1, None, 8, None, 4, None, 5],
    [None, 8, None, None, None, None, None, 7, None],
    [5, None, 9, None, 6, None, 3, None, 1],
    [None, None, None, None, None, 6, 7, 5, None],
    [2, None, None, None, 9, None, None, None, 8],
    [None, None, 6, 8, None, 5, 2, None, 3]
    ]

if __name__ == '__main__':
    solver = SudokuSolver(test_sudoku)
