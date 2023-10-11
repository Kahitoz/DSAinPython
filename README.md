# Speedrunning DSA in Python Programming Language

# Date -> 17th September 
Theories done - 
Lists, -> Square Bracket // mutable
Tuples, -> Curly Bracket // Immutable
Dicitionary,-> {Key: Values} // mutable
Sets, -> set() // mutable // no repeated values
Stacks -> Can use List, push --> append , pop

# Date -> 20th September
Queue Follows FIFO OR LIFO  Elements adding is done from the rear end Removing is done from frontOperation -> Enqueue and Dequeue, isFull, isEmpty Enqueue -> append method, dequeue -> pop method: list.pop(0)

# Priority Queue
In Priority the elements are the basis of its priority
Best Method is to import the Priority Queue instead of using the sort method

# Linked List
Three types - Singly, Double and circular
Singly Linked List -> Node have two parts, data and next. node.data -> Will give the value of the node while printing node simply will only give you the memory reference of that object
 
 *Adding Elements in the Beginning of the Linked List ->
    To add the elements in the beginng of the linked list make a new node point the next of the new node towards the head of the linked list then equate the head to the new node. Now your new node will be the head of the linked list
 *Adding Elements in the end of the Linked List-> To add the elements in the end of the linked      list first we need to reach at the end of the list. To do so we need to make copy node, lets call it a pointer for now and equate it to head of the list(given its not empty, if it is empty then first we need to fill the head) now run a while loop until and unless pointer.next is not null. As soon as pointer.next is null you need to equate it to the new node.

