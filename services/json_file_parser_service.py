from io import UnsupportedOperation
import json
import csv
from typing import List

def parse(file: str, file_format: int) -> List[List[int]]:
    """
    This function will read in the JSON file and parse it into Python dictionary and returns whatever in the data property.
    Arguments:
        file: A path to file to read
        file_format: The file format to use (1: JSON, 2: CSV)
    Returns:
        The sudoku represented in 2D list
    """
    match(file_format):
        case 1:
            json_file_path = f"{file}.json"
            try:
                with open(json_file_path, 'r') as f:
                    loaded_file = json.load(f)

                return loaded_file["data"]
            except FileNotFoundError:
                raise Exception("File not found at given location. Please make sure file exists at the given path and rerun the program.")
        case 2:
            csv_file_path = f"{file}.csv"
            result = []
            try:
                with open(csv_file_path,'r') as csv_file:
                    reader = csv.reader(csv_file)
                    for row in reader:
                        result.append(list(map(int, row)))
                    return result
            except FileNotFoundError:
                raise Exception("File not found at given location. Please make sure file exists at the given path and rerun the program.")

    raise UnsupportedOperation("Format type selected was not supported")

