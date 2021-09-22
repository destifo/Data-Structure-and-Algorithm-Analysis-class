class StackArray:

    def __init__(self):
        self.lst = list()
        self.top = -1

    def isEmpty(self):
        if self.top == -1:
            return True
        return False

    def top(self):
        if self.isEmpty:
            return "Empty list"
        return self.lst[self.top]

    def push(self, key):
        self.top += 1
        self.lst.append(key)

    def pop(self):
        if self.isEmpty():
            return "Empty list!"
        temp = self.lst[self.top]
        self.top -= 1
        self.lst.pop(self.top)
        return temp

    def size(self):
        return self.top + 1
