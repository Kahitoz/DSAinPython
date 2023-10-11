class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def add_elements(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = new_node
    def print_elements(self):
        pointer = self.head
        if self.head is not None:
            while pointer is not None:
                print(pointer.data, end = " ")
                pointer = pointer.next
        else:
            print("Linked List is empty")

LL1 = LinkedList()
for i in range(0, 10):
    LL1.add_elements(i+1)

LL1.print_elements()


