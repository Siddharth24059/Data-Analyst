# This is Example of Nested If else

marks = eval(input('Enter the marks:'))
if marks <=100:
    if marks>=90 and marks<=100:
        print('Grade A')
    elif marks>=80 and marks<=89:
        print('Grade B')
    elif marks>=70 and marks<=79:
        print('Grade C')
    elif marks>=60 and marks<=69:
        print('Grace D')
    elif marks>=50 and marks<=59:
        print('Grade E')
    else:
        print('Failed')
else:
    print('Invalid Marks, Marks should be between 0 to 100')