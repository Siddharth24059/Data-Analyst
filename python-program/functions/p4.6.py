import sys

def add(x,y):  #positional argument
    print(f'x={x} and y={y}')
    return x+y #addition no difference in output because sum follows cummutative law
#(x+y)=(y+x)


def main():
    result=add(10,20)
    print('result 1',result)
    result=add(20,10)
    print('result 2',result)
    
    
sys.exit(main())    