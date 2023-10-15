class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    def print_forward(self):
        if self.head is not None:
            pointer = self.head
            while pointer is not None:
                print(pointer.data,end = " ")
                pointer = pointer.next
            print()
        else:
            print("No elements present in the list")

DLL = DoublyLinkedList()
for i in range(0,10):
    DLL.insert_front(i+1)
DLL.print_forward()
                
