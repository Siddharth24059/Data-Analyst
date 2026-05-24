# wap in python to show the compile time argument 


import sys 

argv = sys.argv #argument variable : list of arguments
argc = len(sys.argv) #argument count

type = type(argv)
print('The Type of c-args:',type)

print('List of arguments:',argv)
print('lenght or size of argument:',argc)