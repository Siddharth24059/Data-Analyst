# if we provide the two numbers then input function will convert them into 
# string value due to which it will be, concatinated,
# So we can resolve this problem by explicitly converting the type of 
# string to int type or float type

no1 = input('Enter the first no:')
no2 = input('Enter the second no:')
print('Result :',no1+no2)

# Note : '+' operator is used for both addition and concatinating the string.
# str + str -> str
# int + int -> int
# str + int -> error



