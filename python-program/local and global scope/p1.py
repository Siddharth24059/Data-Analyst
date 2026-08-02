# Local scope vs global scope
# Note variable are Readonly
import sys 

b = 20 # b is global scope

def display():
    x=10  # local variable
    print(f' x is local to display :{x}')
    print(f'b is at global scope :{b}')


def show():
    a = 100
    print(f'a is local to show :{a}')
    print(f'b is at global scope :{b}')
 
def main():
    display()
    show()

sys.exit(main())