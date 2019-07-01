from .node import Node


class LinkedList:

    def __init__(self, value=None):
        self.count = 0
        self.head = Node(value)
        self.tail = Node()

    def add_last(self, value):
        if self.count == 0:
            self.head.add_value(value)
            self.tail.next = self.head
        else:
            new_node = Node(value)
            self.tail.next.next = new_node
            self.tail.next = new_node
        self.count += 1

    def add_first(self, value):
        next_node = self.head
        self.head = Node(value, next_node=next_node)
        self.count += 1
        if self.count == 1:
            self.tail.next = self.head

    def clear(self):
        self.head = self.tail.next = None
        self.count = 0

    def peek(self):
        return self.head.value

    def peek_last(self):
        return self.tail.next.value

    def pop_last(self):
        if self.count > 0:
            value = self.peek_last()
            if self.count == 1:
                self.head = None
                self.tail = None
            else:
                current = self.head
                while current.next.next is not None:
                    current = current.next
                current.next = None
                self.tail.next = current
            self.count -= 1
            return value

    def pop_first(self):
        if self.count > 0:
            value = self.peek()
            if self.count == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            self.count -= 1
            return value
