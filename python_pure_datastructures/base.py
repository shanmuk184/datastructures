class BaseLinkedListNode:
    def __init__(self):
        self.__data = None
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next):
        self.__next = next
