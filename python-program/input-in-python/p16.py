# Concept of list of comprehension 
# This is short hand of creating the dynamic list in python 

even_list = []
for i in range(0,11,2):
    even_list.append(i)

print(even_list)

# list comprehension
even_list = [i for i in range(0,11,2)]
print(even_list)