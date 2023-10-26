#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """where the class Square is built"""

    def __init__(self, size=0):
        """initialize new Square

        Args:
            size(int): size of new square"""
        self.__size = size

    @property
    def size(self):
        """Get or Set current size of Square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Return current area of Square"""
        return self.__size ** 2
