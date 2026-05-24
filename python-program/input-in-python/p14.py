#wap in Python to show that argument list is a homogenous in nature


import sys 

argv = sys.argv #argument variable : list of arguments
argc = len(sys.argv) #argument count

s_type = input('Enter the type to check:')
print('Selected Type:',s_type)

counter = 0
for i in argv:
    print(f'Type of {i} is {type(i)} = {isinstance(i,eval(s_type))}')
    if isinstance(i,eval(s_type)):
        counter = counter + 1

if counter == argc:
    print('List is Homogenous')
else:
    print('List is Not Homogenous')
    