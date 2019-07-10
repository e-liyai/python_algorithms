from .LinkedList import LinkedList
from .queue import Queue


class Graph:

    def __init__(self):
        self.linkedListDict = dict()

    def add_vertice(self, vertex, values):
        linked_list = LinkedList()
        for value in values:
            linked_list.add_last(value)

        self.linkedListDict[vertex] = linked_list

    def breadth_first_search(self, value):
        queue = Queue()
        if self.linkedListDict:
            for key, value in self.linkedListDict:
                queue.add(value.pop_first())


