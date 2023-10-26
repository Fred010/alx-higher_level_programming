#!/usr/bin/python3

"""Define class Square"""


class Square:
    """where class Square is built"""

    def __init__(self, size=0):
        """initialize new Square

        Args:
            size(int): size of new Square
            """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
