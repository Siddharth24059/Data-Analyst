# Dynamic Type Casting : Automatic conversion of the type by looking into value.

Awnish = 100
print(Awnish)

nadeem = 'Ravi' # string value
print(nadeem)
print(type(nadeem))

x = input('Enter some value:')
print(x)
print(type(x)) # <class 'str'>
result = eval(x) # eval() is used by dynamic type casting
print(f'converted type : {type(result)}')



