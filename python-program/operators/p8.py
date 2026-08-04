# Example of Special Operators :-=
# Identity Operators : is  and is not 

# This concept is related to Memory Address 
# Value same to same ---> is ---> same
# Value is not same to same ---> is not : different 

print(id(10))
x=10
y=x 
print('Memory Address of x=',id(x))
print('Memory Address of y=',id(y))
# print(x is y)

print('is x as y :', x is y)

print('Memory Address of 20=',id(20))
z=20
print('Memory Address of z=',id(z))
print('Memory Address of x=',id(x))
print('is z as x :', z is x) # False because value is different and memory address is different
print('is z as x :', z is not x) # True because value is different and memory address is different