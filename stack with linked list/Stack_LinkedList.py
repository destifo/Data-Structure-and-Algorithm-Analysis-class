from node import Node


class StackedLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def insert(self, value):
        node = Node(value)
        if self.isEmpty():
            self.head = node
        else:
            temp = self.head
            self.head = node
            node.next = temp

    def top(self):
        temp = self.head
        return temp.data

    def pop(self):
        if self.isEmpty():
            return "Empty List"
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            return temp.data
