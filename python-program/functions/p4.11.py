# Different Type of arguments in Python 
#  variable length Named argument
import sys 

def add(**d): 
    print('type:',type(d))
    print(d)
    return d['x'] + d['y'] #d is a dictionary and we can access the value by using the key

    
    
def main():
    result = add(y=10,x=20) #x=10 and y=20 | position depend
    print(result)

sys.exit(main())