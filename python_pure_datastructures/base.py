
class BaseNode(object):
    def __init__(self):
        self.__data = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

class BaseLinkedListNode(BaseNode):
    def __init__(self):
        super().__init__()
        self.__next = None

    def get_next(self):
        return self.__next

    def set_next(self, next):
        self.__next = next

class DoubleLinkedListNode(BaseLinkedListNode):
    def __init__(self):
        super().__init__()
        self.__prev = None

    def get_prev(self):
        return self.__prev

    def set_prev(self, prev):
        self.__prev = prev

class BaseLinkedList:
    def __init__(self):

        self.length = 0

    def create_node(self, data):
        pass
    def insert_at_end(self, data):
        node = self.create_node(data)
        if not self.head:
            self.head = node
        else:
            self.set_nth_node(self.head, node, self.length-1)
        self.length += 1
        return self.length


    def set_nth_node(self, node_to_iterate, node_to_insert,  n):
        i = 0
        while (i != n):
            node_to_iterate = node_to_iterate.get_next()
            i += 1
        node_to_iterate.set_next(node_to_insert)

    def set_head(self, node):
        if self.head:
            node.set_next(self.head)
            self.head = node
        else:
            self.head = node


    def insertAt(self, data, position=None):
        if position > self.length or position < 0:
            return 'Index out of range'
        node = self.create_node(data)
        if position == 0:
            self.set_head(node)
            return True
        self.set_nth_node(self.head, node, position-1)
        self.length += 1
        return True

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
