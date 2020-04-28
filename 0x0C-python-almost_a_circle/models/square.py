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

    def update(self, *args, **kwargs):
        """
        args and kwargs
        """
        if len(args) != 0:
            for i, v in enumerate(args):
                if i == 0:
                    self.id = v
                if i == 1:
                    self.size = v
                if i == 2:
                    self.x = v
                if i == 3:
                    self.y = v
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = kwargs[k]
                if k == "size":
                    self.size = kwargs[k]
                if k == "x":
                    self.x = kwargs[k]
                if k == "y":
                    self.y = kwargs[k]

    def to_dictionary(self):
        """
        return dict representation
        """
        return {"id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y, }
