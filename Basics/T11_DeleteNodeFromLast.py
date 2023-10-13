class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def delete_last(self):
        if self.head is None:
            print("List is Empty")
            return
        if self.head.next is None:
            self.head = None
            return
        new_node = None
        pointer = self.head
        while pointer.next.next is not None:
            pointer = pointer.next
        pointer.next = new_node

    def add_Nodes(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = new_node

    def print_nodes(self):
        if self.head is not None:
            pointer = self.head
            while pointer is not None:
                print(pointer.data, end =" ")
                pointer = pointer.next
        else:
            print("No elemets  in the list")

LL1 = LinkedList()
for i in range(0,10):
    LL1.add_Nodes(i+1)
LL1.print_nodes()
print()
n = input()
while n != "Exit":
    n = input()
    if n == "Delete":
        print()
        LL1.delete_last()
        LL1.print_nodes()
        print()
    elif n == "Exit":
        print("Goodbye")
    else:
        print("Invalid")
        