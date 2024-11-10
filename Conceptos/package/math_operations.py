from typing import Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Returns the sum of two numbers.
    :param a: First number (float).
    :param b: Second number (float).
    :return: The sum of a and b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("Expected first argument to be a numeric type.")

    if not isinstance(b, (int, float)):
        raise TypeError("Expected first argument to be a numeric type.")

    return a + b


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Returns the difference between two numbers.
    :param a: First number (float).
    :param b: Second number (float).
    :return: The difference between a and b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("Expected first argument to be a numeric type.")

    if not isinstance(b, (int, float)):
        raise TypeError("Expected first argument to be a numeric type.")

    return a - b
