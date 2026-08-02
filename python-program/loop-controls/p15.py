#for loop with list 

l =[1,2,3,4,5]
for i in l:
    print(f'the value of item = {i}')

# with dictionary
d = {'name':'Awnish','age':50,'marks':80}

# to print key and value both
for item in d.items():
    print(f'item = {item}')
    key,value = item
    print(f'key = {key} and value={value}')

# to print key and value both
for key,value in d.items():
    print(f'key = {key} and value={value}')

# to print only keys
for key in d.keys():
    print(f'key = {key}')

# to print only values
for value in d.values():
    print(f'value = {value}')


# How to get value from key in dictionary
for key in d:
    print(f'key = {key} and value={d[key]}')
