#!/usr/bin/python3
"""This module contains classes for a singly linked list."""


class Node:
    """This class defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a new instance of the Node class."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method for retrieving the data attribute."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method for setting the value of the data attribute."""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter method for retrieving the next_node attribute."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method for setting the value of the next_node attribute."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """This class defines a singly linked list."""

    def __init__(self):
        """Initializes a new instance of the SinglyLinkedList class."""
        self.head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position"""
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Returns a string representation of the linked list."""
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
