class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def insertData(self, data):
        if isEmpty():
            node = Node(data)
            this.head = node
        else:
            temp = self.head
            while (temp.next == !None):
                temp = temp.next
            temp.next = node

    def insertHead(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def deleteKey(self, key):
        if isEmpty():
            return "Empty list"
        temp = self.head
        prev = temp
        while temp.next != None:

            if self.head == temp and temp.data == key:
                self.head = temp.next
                temp.next = None
                prev = self.head
            else:
                temp = temp.next
                if temp.data == key:
                    prev.next = temp.next
                    temp.next = None
                else:
                    prev = temp
                    #temp = temp.next
