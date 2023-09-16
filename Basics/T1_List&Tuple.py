# List Begins Here

# some statements to print later
statement_1 = "Using parameter the list values are - "
statement_2 = "Using the list constructor - "
statement_3 = "Any type of data types to get stored in list- "
statement_4 = "Lists are ordered"

# Simple list initialization using square brackets and adding elements
list_1 = [1,2,3,4,5,6,7,8,9]
print(statement_1,list_1)

# Initializing the list using the constructor
list_2 = list()

for i in range(1,10):
    list_2.append(i)

print(statement_2,list_2)    

# any type of data can get stored inside list
list_3 = [1,2,'Hi',3.5]
print(statement_3,list_3)

# Lists are ordered
print(list_1==list_2)

# Lists are mutabel, i.e you can modify the list
# Lists are dynamic

# Lists ends here

# Tuple starts here
state_1 = "Tuples are created using paranthesis"

# Initializing the tuple using the paranthesis
tuple_1 = (1,2,3,4,5)
print(state_1,tuple_1)
print(type(tuple_1))

# Using the constructor 
tuple_2 = 1,2,3,4,5,6,7,8,9
print(tuple(tuple_2))

# tuples are immutable i.e their state cannot be changed after creation

# tuples are faster then the list
# sometimes we dont need data to be modified