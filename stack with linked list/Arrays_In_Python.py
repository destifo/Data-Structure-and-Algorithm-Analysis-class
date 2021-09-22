class Array:

    def __init__(self, indexNo):
        self.indexNo = indexNo
        self.lst = [None] * indexNo
        self.lastIndex = 0

    def add(self, key, position = None):
        if position == None:
            position = self.lastIndex

        if position > self.indexNo - 1:
            return "Value insertion isn't Possible!"
        if self.lastIndex == self.indexNo - 1:
            return "Array is full"
        if self.lastIndex == self.indexNo - 2:
            self.lst[position] = key
            self.lastIndex += 1
            return
        else:
            for i in range(self.lastIndex + 2, position,-1):
                self.lst[i] == self.lst[i - 1]
            self.lst[position] = key
            self.lastIndex += 1
            return

    def remove_key(self, position, key):
        if position > self.indexNo - 1:
            raise IndexError("Index Out Of Bounds")
        if self.indexNo == 0:
            return "Empty Array!"
        if position == self.lastIndex:
            self.lst[position] = None
            self.lastIndex -= 1
            return

        for i in range(self.lastIndex, position - 1, -1):
            self.lst[i - 1] = self.lst[i]

        self.lst[self.lastIndex] = None
        self.lastIndex -= 1

    def at_index(self, index_no):
        assert index_no <= self.lastIndex
        return self.lst[index_no]
