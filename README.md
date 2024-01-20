# Sudoku Solver as Constraint Satisfaction Problem solved using Backtracking and forward checking
## Prerequisite
```
python 3.11+
```

## Design and Assumptions
Assumptions:
- The size of sudoku is 9x9.
- The sudoku is going to be stored in a JSON file under property data or CSV file (default to be JSON).
- The sudoku itself is going to be represented using a 2-D array where each element represent each cell in the sudoku.
- The cell that is not filled is going to be assumed to has a value of 0.
- The output solved sudoku is printed to the screen.

Design:
- The constraints are for each cell, there will be an all-diff constraints on all element in the row and column along with cells in the corresponding 3x3 grids.
- The variable is going to be each cell in the sudoku.
- The algorithm is going to use Minimum Remaining Value for selection.
- The algorithm is going to use Least Contraining Value for value ordering.
- Before searching, arc-consistency algorithm AC3 is going to be performed to prune out all possible initial violation.
- If before failed to find a solution, a backtracking search will be performed.
- Every assignment will trigger a forward check to prune out possible conflicts.
- Since forward checking is performed, a simple backjumping is going to be redundant therefore a simple backtracking is used instead.

## Usage

### Options
Belows are the possible options that came along with the implementation:

```
usage: main.py [-h] [-d DATA] [-f FORMAT]

options:
  -h, --help            show this help message and exit
  -d DATA, --data DATA  The path to boxes JSON file for testing
  -f FORMAT, --format FORMAT
                        The format of the input file (1: JSON, 2: CSV)
```

File format can be 1 or 2

### Examples
To run with regular sudoku json:
```
python main.py -d data.json
```

To run with the evil sudoku json:
```
python main.py -d evil_sudoku
```

To run with the regular sudoku csv:
```
python main.py -f 2
```

To run with the evil sudoku csv:
```
python main.py -d evil_sudoku -f 2
```


