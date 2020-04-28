#!/usr/bin/python3
"""
square class
"""


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    square class inheret
    from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    @property
    def size(self):
        """
        get size
        """
        return self.height

    @size.setter
    def size(self, size):
        """
        set size
        """
        self.width = size
        self.height = size
