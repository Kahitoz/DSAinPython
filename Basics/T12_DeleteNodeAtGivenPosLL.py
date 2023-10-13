class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def find_length(self):
        pointer = self.head
        counter = 0
        while pointer is not None:
            pointer = pointer.next
            counter = counter+1
        return counter

    def delete_at_pos(self,pos):
        if self.head is None:
            print("List is Empty")
        elif pos>self.find_length():
            print("Invalid position, current Length of List is = ",self.find_length())
        
        elif pos == 0:
            pointer = self.head
            if pointer.next is not None:
                pointer = pointer.next
                self.head = pointer
            else:
                self.head = None
        else:
            pointer = self.head
            p_pointer = self.head
            while pos > 0:
                p_pointer = pointer
                pointer = pointer.next
                pos = pos-1
            if p_pointer is None:
                self.head = pointer.next
            else:
                p_pointer.next = pointer.next


    def add_node(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            pointer = self.head
            while pointer.next != None:
                pointer = pointer.next
            pointer.next = new_node
    
    def print_node(self):
        pointer = self.head
        while pointer is not None:
            print(pointer.data, end=" ")
            pointer = pointer.next
        
LL1 = LinkedList()
for i in range(0,1):
    LL1.add_node(i)

LL1.print_node()
print()
LL1.delete_at_pos(0)
print()
LL1.print_node()

