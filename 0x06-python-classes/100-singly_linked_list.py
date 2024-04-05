#!/usr/bin/python3

class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) == int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value != None and type(value) != Node:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value

class SinglyLinkedList:

    def __init__(self):
        self.__head = None

    def __str__(self):
        temp = self.__head
        h_list = []

        while temp:
            h_list.sort()
            h_list.append(str(temp.data))
            temp = temp.next_node
        h_list.sort(key=int)
        return ("\n".join(h_list))

    def sorted_insert(self, value):
        new_node = Node(value)

        if self.__head == None:
            new_node.next_node = self.__head
            self.__head = new_node

        else:
            new_node.data = value
            new_node.node_next = self.__head
            self.__head = new_node

