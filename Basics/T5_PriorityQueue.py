# Works in the basis of first in first out method
# In Priority the elements are the basis of its priority

# Best Method is to import the Priority Queue instead of using the sort method

import queue
q = queue.PriorityQueue()
counter = 10
for i in range(0,10):
    q.put(counter*10)
    counter = counter-1

print(q.get())
