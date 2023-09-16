# Stacks follows First In Last Out

# Stack implementation using list
# push ---> append, pop ---> pop

stack = []
for i in range(0, 11):
    stack.append(i)

print(stack.pop())