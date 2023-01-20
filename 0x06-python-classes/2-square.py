#!/usr/bin/python3


class Square:
    """The Square class represents a square shape in a 2-Dimensional space"""
    def __init__(self, size=0):
        """
        Initializes a square with an optional size
        :param size: the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
