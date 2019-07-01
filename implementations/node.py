class Node:

    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node

    def add_node(self, node):
        self.next = node

    def remove_next_node(self):
        self.next = None

    def add_value(self, value):
        self.value = value
