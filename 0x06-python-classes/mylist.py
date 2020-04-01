#!/usr/bin/python3
class Node:
    """Create a Node obkect."""
    def __init__(self, data, next_node=None): #self.next_node ??
        """put Node data structrure"""
        self.data = data
        self.next_node = next_node

    @property
    def next_node(self):
        """retrive next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """define next node parameters"""
        if type(value) != Node and type(value) != None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

    @property
    def data(self):
        """define data"""
        return self.__data

    @data.setter
    def data(self, value):
        """define data structure"""
        if type(value) != int:
            raise TypeError("data must be integer")
        else:
            self.__data = value

class SinglyLinkedList:
    """define a linked list class """
    def __init__(self):
        """initialize a singly linked list """
        self.__head = None

    def sorted_insert(self, value):
        """Insert element in nodes"""
        new_node = Node(value)
        cur = self.__head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
        curent = self.__head
        while curent:
            print(curent.data)
            curent = curent.next
        

        
#rest is to add nodes/ then retrive all the data inserted and print it sorted one per line        
