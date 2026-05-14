# different type of argument in python 
# default is always at last
#default argument is also treated as optional argumnet 

import sys

#definition of function 
#x:mendatory
#y:mendatory
#z:optional-> if values is supplied then i will take your value otherwise i will use 
# my default value

def add(x,y,z=0):  #positional argument
    print(f'x={x} and y={y} and z={z}')
    return x+y+z #addition no difference in output because sum follows cummutative law
#(x+y)=(y+x)


def main():
    #calling
    result=add(10,20)#no value supply : z default:0
    print(result)
    result=add(20,10,5)#z=0 will be replace by 5
    print(result)
    
    
sys.exit(main())    