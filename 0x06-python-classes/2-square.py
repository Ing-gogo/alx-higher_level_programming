#!/usr/bin/python3
"""square class"""


class Square:
    """Representing a square"""

    def__init__(self, size=0):
        """initializing a square
        Args:
            size(int): size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
