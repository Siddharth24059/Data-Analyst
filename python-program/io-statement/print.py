import builtins
#builtin module is an important module which contains the definition 
# all builtin function.

original_print = print
# print('This is print')
# original_print('This is Original print')

def my_print(*args,**kwargs):
    original_print('Argument Count:',len(args))
    original_print(*args,**kwargs)


builtins.print = my_print

# Now This print function with tell no of arguments 

print('siddharth','Kumar','jaiswal',sep=' ') # 2
print('siddharth','Kumar','jaiswal',sep='') # 2
print('siddharthKumar',sep='@')
print('siddharth'+'Kumar',sep='#')


print('Hello','world')  
print('Hello','world',sep='-')
print('A','B','C')
print('with backslash n A','B','C',sep='\n')
# Tricky concepts.
print('without backslash n A','B','C',sep=chr(10))












 