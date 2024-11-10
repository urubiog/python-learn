from typing import List


def read_file(path: str) -> str:
    """
    Reads the content of a file and returns it as a string.
    :param file_path: The path to the file (str).
    :return: The content of the file.
    """
    try:
        with open(path, "r") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {path} was not found.")
    except IOError:
        raise IOError(f"Could not read the file at {path}.")


def write_file(file_path: str, content: str) -> None:
    """
    Writes content to a file, overwriting it if it exists.
    :param file_path: The path to the file (str).
    :param content: The content to write to the file (str).
    :return: None
    """
    try:
        with open(file_path, "w") as file:
            file.write(content)
    except IOError:
        raise IOError(f"Could not write to the file at {file_path}.")
