# named or keyword argument: in named argument we refer the value by name not by positon.
#we will explicitly say x=10 y=20
#in named argument it does not depend on the value






import sys

def add(x,y):  #named argument
    print(f'x={x} and y={y}')
    return x+y #addition no difference in output because sum follows cummutative law
#(x+y)=(y+x)


def main():
    result=add(x=10,y=20)
    print('result 1',result)
    result=add(y=20,x=10)
    print('result 2',result)
    
    
sys.exit(main())    