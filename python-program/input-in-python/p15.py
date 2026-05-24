#wap in Python to show that argument list is a homogenous in nature


import sys 

argv = sys.argv #argument variable : list of arguments
argc = len(sys.argv) #argument count

counter = 0
for i in argv:
    print(f'Type of {i} is {type(i)} = {isinstance(i,str)}')
    if isinstance(i,str):
        counter = counter + 1

if counter == argc:
    print('List is Homogenous')
else:
    print('List is Not Homogenous')
    