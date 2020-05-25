from .base import BaseLinkedListNode

class SinglyLinkedListNode(BaseLinkedListNode):
    pass

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def create_node(self, data):
        node = SinglyLinkedListNode()
        node.set_data(data)
        return node

    def insert(self, data):
        node = self.create_node(data)
        if not self.head:
            self.head = node
            i = 1
        else:
            node_to_iterate = self.head
            i = 0
            while (node_to_iterate.get_next()):
                node_to_iterate = node_to_iterate.get_next()
                i += 1
            node_to_iterate.set_next(node)
        self.length += 1
        return i + 1

    def insertAt(self, data, position=None):
        if position > self.length or position < 0:
            return 'Index out of range'

        node = self.create_node(data)

        if position == 0:
            if self.head:
                node.set_next(self.head)
                self.head = node
                return 1
            self.head = node
            return 1
        i = 0
        node_to_iterate = self.head
        while (i != position-1):
            node_to_iterate = node_to_iterate.get_next()
            i += 1
        node.set_next(node_to_iterate.get_next())
        node_to_iterate.set_next(node)
        self.length += 1
        return i+1

    def print_list(self):
        node_to_print = self.head
        while(node_to_print):
            print(node_to_print.get_data())
            node_to_print = node_to_print.get_next()

    def delete_from_beginning(self):
        if not self.head:
            return 'No elements are there'
        self.head = self.head.get_next()
        return True

    def delete_from_end(self):
        if not self.head:
            return 'No elements are there'
        node = self.head
        while(node.get_next().get_next()):
            node = node.get_next()
        node.set_next(node.get_next().get_next())
        return True

    def set_nth_node(self, node_to_iterate, node_to_insert):
        while (node_to_iterate.get_next()):
            node_to_iterate = node_to_iterate.get_next()
        node_to_iterate.set_next(node_to_insert)

    def delete_at(self, pos):
        if pos >= self.length or pos < 0:
            return 'Index out of range'
        if pos == 0:
            self.delete_from_beginning()
        elif pos == self.length-1:
            self.delete_from_end()
        else:
            i = 0
            node = self.head
            while (i != pos-1):
                node = node.get_next()
            node.set_next(node.get_next().get_next())
        return 1
# from python_pure_datastructures.linked_list import SingleLinkedList
linkedlist = SingleLinkedList()
linkedlist.insert_at_end(1)
linkedlist.insert_at_end(2)
linkedlist.insertAt(3,1)
linkedlist.insertAt(3,4)
linkedlist.print_list()