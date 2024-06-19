from pathlib import Path

ROOT_DIR = str(Path(__file__).resolve().parent.parent.parent)
# print(ROOT_DIR)

def get_path(relative_path):
    """
    The function `get_path` concatenates the `ROOT_DIR` with a given `relative_path` to return the full
    path.
    
    Args:
      relative_path: The `relative_path` parameter is a string that represents the path to a file or
    directory relative to the root directory.
    
    Returns:
      The function `get_path` is returning the result of concatenating the `ROOT_DIR` with the
    `relative_path` parameter.
    """
    
    if not relative_path.startswith("/"):
        relative_path = "/" + relative_path
    
    return ROOT_DIR + relative_path