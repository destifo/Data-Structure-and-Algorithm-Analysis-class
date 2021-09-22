from node import Node


class StackedLinkedList:
    def __init__(self):
        self.head = None
        self.last_index = -1

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def insert(self, value):
        node = Node(value)
        if self.isEmpty():
            self.head = node
            self.last_index += 1
        else:
            temp = self.head
            self.head = node
            node.next = temp
            self.last_index += 1

    def top(self):
        temp = self.head
        return temp.data

    def size(self):
        if self.isEmpty(): return 0
        return self.last_index + 1

    def pop(self):
        if self.isEmpty():
            return "Empty List"
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.last_index -= 1
            return temp.data
