#!/usr/bin/python3

"""Define class Square"""


class Square:
    """ where the class Square is built"""

    def __init__(self, size=0):
        """initialize new square

        Args:
            size(int): size of new square"""
        self.__size = size

    @property
    def size(self):
        """Get or Set current size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns current area of square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with # character"""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()
