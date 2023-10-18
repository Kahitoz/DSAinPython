class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        print(l1.head.val)
       
        

class CreateLinkedList:
    def __init__(self):
        self.head = None
    def add_node(self,data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = new_node
    def print_list(self):
        pointer = self.head
        while pointer is not None:
            print(pointer.val, end = " ")
            pointer = pointer.next

L1 = CreateLinkedList()
L2 = CreateLinkedList()
for i in range(1,4):
    L1.add_node(i*2)
    L2.add_node(i*3)
L1.print_list()
print()
L2.print_list()
Sol = Solution()
Sol.addTwoNumbers(L1,L2)

