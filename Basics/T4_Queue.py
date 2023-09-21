# Follows FIFO OR LIFO 
# Elements adding is done from the rear end
# Removing is done from front
# Operation -> Enqueue and Dequeue, isFull, isEmpty
# Enqueue -> append method, dequeue -> pop method: list.pop(0)

queue = []
for i in range(0,10):
    queue.append(i)

print(queue)

print(queue.pop(0))
print(queue.pop(0))

# Method 2 inserting the method from the front side and removing the method from the back side
another = []
for i in range(0, 10):
    another.insert(0, i)

print(another)
