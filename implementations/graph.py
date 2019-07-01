from .LinkedList import LinkedList


class Graph:

    def __init__(self):
        self.linkedListDict = dict()

    def add_vertice(self, vertex, values):
        linked_list = LinkedList()
        for value in values:
            linked_list.add_last(value)

        self.linkedListDict[vertex] = linked_list
