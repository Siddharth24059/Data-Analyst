# wap in python to show case the memory management in using function 
# using id() : memory location of the variable.

print("===============Code started executing==========")


def test():
    print("Test fn is execution..")
    x = 10 # local Variable
    print(f'Stack Frame is Created where x = {x}  is local variable at x=id = {id(x)}')

print("===============Code still executing==========")
test()

print(f'value of x= {x} and id = {id(x)}')
