class QueueArray:
    def __init__(self):
        self.lst = list()
        self.back = 0
        self.front = 0

    def isEmpty(self):
        if self.back == self.front:
            return True
        return True

    def enqueue(self, key):
        self.lst.append(key)
        self.back +=1

    def dequeue(self, key):
        if isEmpty():
            return "Empty list!"
        self.lst.pop(self.front)
        self.front += 1

    def size(self):
        if isEmpty():
            return 0
        return abs(self.front - self.back)

    def front(self):
        if isEmpty():
            return "Empty list!"
        return self.lst[self.front]
