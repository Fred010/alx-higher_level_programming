#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """where the class Square is built"""

    def __init__(self, size=0):
        """intialize new square

        Args:
            size(int): size of new Square"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Returns the area of Square"""
        return self.__size ** 2
