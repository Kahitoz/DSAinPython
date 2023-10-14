class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_front(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            pointer = self.tail
            while pointer.prev is not None:
                pointer = pointer.prev
            pointer.prev = new_node
            new_node.next = pointer
            self.tail = new_node

                
