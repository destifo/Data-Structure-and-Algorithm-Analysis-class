class QueueArray:
    def __init__(self):
        self.lst = list()
        self.back = -1
        self.front = -1

    def isEmpty(self):
        if self.back == self.front:
            return True
        return False

    def enqueue(self, key):
        self.lst.append(key)
        self.back += 1

    def dequeue(self):
        if self.isEmpty():
            return "Empty list!"
        self.lst[self.front] = None
        self.front += 1

    def size(self):
        if self.isEmpty():
            return 0
        return abs(self.front - self.back)

    def front(self):
        if self.isEmpty():
            return "Empty list!"
        return self.lst[self.front]

    def top(self):
        if self.isEmpty(): return "Empty Queue"
        return self.lst[self.back]
