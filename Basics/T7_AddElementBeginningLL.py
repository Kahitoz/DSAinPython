class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    
    def print(self):
        if self.head is not None:
            pointer = self.head
            while pointer is not None:
                print(pointer.data)
                pointer = pointer.next
        else:
            print("The List is Empty")

LL1 = LinkedList()
LL1.add_beginning(10)
LL1.add_beginning(20)
LL1.print()

