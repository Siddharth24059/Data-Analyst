# Prime Number using Nested if else
# Prime Number is a number which is divisible by 1 and itself only. It should be greater than 1.


# 1 to 100 : How many prime numbers are there?
# 25 : Prime Numbers

# if any number 2,3,5,7
number = int(input('Enter the No:'))

if number > 1 and number <= 100:
    # print('No is Valid')
    if number % 2 == 0 :
        if number == 2:
            print('No is Prime')
        else:
            print('No is not Prime')
    elif number % 3 == 0:
        if number == 3:
            print('No is Prime')
        else:
            print('No is not Prime')
    elif number % 5 == 0:
        if number == 5:
            print('No is Prime')
        else:
            print('No is not Prime')
    elif number % 7 == 0:
        if number == 7:
            print('No is Prime')
        else:
            print('No is not Prime')
    else:
        print('No is Prime')
else:
    print('No is not Valid')