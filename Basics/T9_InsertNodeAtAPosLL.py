class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def length_ll(self):
        if self.head is None:
            return 0
        else:
            pointer = self.head
            counter = 0
            while pointer is not None:
                pointer = pointer.next
                counter = counter+1
            return counter
    
    def insert_nodes(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = new_node
    
    def at_a_given_pos(self, pos, data):
        new_node = Node(data)
        if self.head is None:
            print("Nothing in the list")
        elif self.length_ll() < pos:
            print("Invalid Pos")
        else:
            pointer = self.head
            while pos>1:
                pointer = pointer.next
                pos     = pos-1
            new_node.next = pointer.next
            pointer.next  = new_node
    
    def print_ll(self):
        if self.head is not None:
            pointer = self.head
            while pointer is not None:
                print(pointer.data, end =" ")
                pointer = pointer.next
        else:
            print("List is Empty")

LL2 = LinkedList()
for i in range(0,10):
    LL2.insert_nodes((i+1)*10)
LL2.at_a_given_pos(3, 35)
LL2.print_ll()

    
            
        
        
    