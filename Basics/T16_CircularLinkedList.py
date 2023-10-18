class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class CircularLinkedList:
    def __init__(self):
        self.head = None
    def add_Nodes(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = new_node
    def create_circular_list(self):
        if self.head is None:
            print("Nothing in the list")
        else:
            pointer = self.head 
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = self.head
    def print_nodes(self):
        if self.head is not None:
            pointer = self.head
            counter = 0
            while pointer is not None:
                if counter != 100:
                    print(pointer.data, end = " ")
                    pointer = pointer.next
                    counter += 1
                else:
                    break

CL1 = CircularLinkedList()
for i in range (0,10):
    CL1.add_Nodes(i)

CL1.create_circular_list()
CL1.print_nodes()
            