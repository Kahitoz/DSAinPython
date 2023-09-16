# Dicitionary starts here

s_dict1 = "The name is - "

# Using curly bracket, key and value pair
dict_1 = {"name":"Kshitiz", "age":21, "gender":"male"}
print(dict_1)

# calling the values with keys
print(s_dict1,dict_1.get("name"))

# keys should be unique or else the last value of the key will get printed

# dictionaies are unorderd
dict_2 = {"gender":"male", "name":"Kshitiz", "age":21}  
print(dict_2==dict_1)

# Dictionary ends here

# Sets states here

# Using curly brackets
set_1 = {1,2,3,4,5,6,7}
print(set_1)

# using constructor, removes repeated letter
set_2 = set("hello")
print(set_2)

set_3 = {'s', 's', 'a', 'b'}
print(set_3)

# They are mutable
# They are unordered