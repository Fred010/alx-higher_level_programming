#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """shows a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
    """

    num_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialize a new Rectangle.

        Args:
            width (int): width of the new rectangle.
            height (int): height of the new rectangle.
        """
        type(self).num_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or Set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get or Set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """returns the output of the Rectangle.

        shows the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """outputs the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """outputs a message for every deletion of a Rectangle."""
        type(self).num_of_instances -= 1
        print("Bye rectangle...")
