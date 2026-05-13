import sys


def add(x,y):
    return x+y


def main():
    no1=eval(input("Enter first number: "))
    no2=eval(input("Enter second number: "))
    result=add(no1,no2)
    print(f'The result is: {result}')
sys.exit(main())    