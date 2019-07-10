class Queue:
    def __init__(self):
        self.list = list()
        self.count = 0

    def add(self, value):
        self.list.append(value)
        self.count += 1

    def peek(self):
        if self.count:
            return self.list[0]
        return None

    def pop(self):
        if self.count:
            self.count -= 1
            return self.list.pop(0)
        return None
