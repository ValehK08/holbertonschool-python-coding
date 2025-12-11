#!/usr/bin/python3
"""SQUAAAARE"""


class Square:
    """SQUAAAAAAAAAAAARE"""

    def __init__(self, size=0):
        """INIT SIIIZE"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        self.size = size

    @property
    def size(self):
        """GEEET IT"""

        return self.__size

    @size.setter
    def size(self, siz):
        """SIIIIZE"""

        if type(siz) is not int:
            raise TypeError("size must be an integer")
        elif siz < 0:
            raise ValueError("size must be >= 0")
        self.__size = siz

    def area(self):
        """AREAAAAA"""
        return self.__size**2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(size):
                print(self.size * "#")
