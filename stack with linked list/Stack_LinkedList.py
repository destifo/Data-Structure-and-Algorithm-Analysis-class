class StackedLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head == None:
            return True
        return False
    def insert(self, value):
        node = Node(value)
        if isEmpty():
            self.head = node
        else:
            temp = self.head
            self.head = node
            node.next = temp

    def pop(self):
        if isEmpty():
            return "Empty List"
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            return temp.data
