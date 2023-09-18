# Stacks follows First In Last Out

# Stack implementation using list
# push ---> append, pop ---> pop

stack = []
for i in range(0, 11):
    stack.append(i)

print(stack.pop())

# using collection
import collections
s1 = collections.deque()
s1.append(10)
s1.append(20)
s1.append(30)
s1.append(40)
print(s1)
print("Popped Value = :", s1.pop())