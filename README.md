# Sudoku Solver as Constraint Satisfaction Problem solved using Backtracking and forward checking

## Assumptions
- The python version is 3.11+.
- The size of sudoku is 9x9.
- The sudoku is going to be stored in a JSON file under property data.
- The sudoku itself is going to be represented using a 2-D array where each element represent each cell in the sudoku.
- The cell that is not filled is going to be assumed to has a value of 0.
- The constraints are for each cell, there will be an all-diff constraints on all element in the row and column along with cells in the corresponding 3x3 grids.
- The output solved sudoku is printed to the screen.
- The variable is going to be each cell in the sudoku.
- The algorithm is going to use Minimum Remaining Value for selection.
- The algorithm is going to use Least Contraining Value for value ordering.
- Before searching, arc-consistency algorithm AC3 is going to be performed to prune out all possible initial violation.
- If before failed to find a solution, a backtracking search will be performed.
- Every assignment will trigger a forward checking to prune out possible conflicts.
- Since forward checking is performed, a simple backjumping is going to be redundant therefore a simple backtracking is used instead.

## Usage

### Options
Belows are the possible options that came along with the implementation:

```
usage: main.py [-h] [-d DATA]

options:
  -h, --help            show this help message and exit
  -d DATA, --data DATA  The path to boxes JSON file for testing
```

### Examples
To run with regular sudoku:
```
python main.py -d data.json
```

To run with the evil sudoku:
```
python main.py -d evil_sudoku.json
```




