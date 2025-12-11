#!/usr/bin/python3
"""SQUAAAARE"""


class Square:
    """SQUAAAAAAAAAAAARE"""

    def __init__(self, size=0):
        """INIT SIIIZE"""

        self.size(size)

    def size(self):
        """GEEET IT"""

        return self.__x

    def size(self, size):
        """SIIIIZE"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size**2
