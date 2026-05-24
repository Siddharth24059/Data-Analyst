
# return can be only used within the function 
# if we use return without any function it will give error,saying return should a part of functional
# block.

import sys

def main():
    num = eval(input('Enter the value:'))
    if num%2 == 0:
        print(f' {num} is even')
        return
    print(f' {num} is Odd')

sys.exit(main())

