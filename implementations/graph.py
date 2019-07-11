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

    def breadth_first_search(self, search_value):
        keys = list(self.linkedListDict.keys())

        visited = {key: 0 for key in keys}
        queue = Queue()
        value_level = 0

        if self.linkedListDict:
            # first_key, value = self.linkedListDict.popitem()
            # queue.add(first_key)
            # visited[first_key] = 1
            queue.add('bit')
            visited['bit'] = 1

            while queue.count:
                current_node = queue.pop()
                llist = self.linkedListDict[current_node]
                value_level += 1
                if current_node == search_value:
                    return value_level
                while llist.count:
                    current_value = llist.pop_first()
                    if visited[current_value] == 0:
                        visited[current_value] = 1
                        queue.add(current_value)

        return value_level
