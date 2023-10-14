class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def InsertEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = new_node
            new_node.prev = pointer
            self.tail = new_node
    def print_reverse(self):
        if self.tail is not None:
            pointer = self.tail
            while pointer is not None:
                print(pointer.data,end=" ")
                pointer = pointer.prev
            print()
    def print_forward(self):
        if self.head is not None:
            pointer = self.head
            while pointer is not None:
                print(pointer.data, end=" ")
                pointer = pointer.next
            print()
    
DLL = DoublyLinkedList()
for i in range(0,10):
    DLL.InsertEnd(i)

DLL.print_forward()
DLL.print_reverse()
                