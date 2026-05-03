
line = int(input('Enter the line:'))

if line in [1,4,6]:
    print('Line 1 is Executing')
    if line-1 in [2,3]:
        print('\t Line 2 is executing')
        print('\t Line 3 is executing')
        if True:
            print('\t\t Line 5 is executing')
            print('\t\t Line 8 is executing')
    print('Line 4 is Executing')
    print('Line 6 is Executing')