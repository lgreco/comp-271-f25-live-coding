class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return str(self.data)

    def has_next(self):
        return self.next is not None

    def has_prev(self):
        return self.prev is not None

    def is_last(self):
        return self.next is None

    def is_first(self):
        return self.prev is None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_next(self, node):
        self.next = node

    def set_prev(self, node):
        self.prev = node
