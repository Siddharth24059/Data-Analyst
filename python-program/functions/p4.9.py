# Different Type of arguments in Python 
# varaible length argument : we can supply n of arguments
import sys 

def add(*n):  #Positional Argument
    print(n)
    print(type(n))
    print(len(n))
    sum = 0
    for i in n:
        sum = sum+i
    return sum
    
def main():
    result = add(20) #length = 1
    print(result)
    result=add(20,) #length = 2
    print(result)
    result=add(20,10,5) #length = 3
    print(result)
    result=add(20,10,5,15) #length = 4
    print(result)
    result=add(20,10,5,15,25) #length = 5
    print(result)


sys.exit(main())