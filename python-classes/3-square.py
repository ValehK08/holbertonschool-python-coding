#!/usr/bin/python3
"""SQUAAAARE"""


class Square:
    """SQUAAAAAAAAAAAARE"""

    def __init__(self, size=0):
        """INIT SIIIZE"""

        self.size(size)
    
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
        return self.__size**2
