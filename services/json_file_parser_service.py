import json

def parse(file: str):
    """
    This function will read in the JSON file and parse it into Python dictionary and returns whatever in the data property.
    Arguments:
        file: A path to JSON file to read
    Returns:
        The value of the data property.
    """
    with open(file, 'r') as f:
        loaded_file = json.load(f)

    return loaded_file["data"]

