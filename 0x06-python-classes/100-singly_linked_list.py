#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        if type(data) != int:
            raise TypeError("data must be integer")
        else:
            self.__data = data
        if type(next_node) != Node and type(next_node) != None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) != Node and type(value) != None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be integer")
        else:
            self.__data = value

class SinglyLinkedList:
    def __init__(self):
        self.head = None
#rest is to add nodes/ then retrive all the data inserted and print it sorted one per line        
