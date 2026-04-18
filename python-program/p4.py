# primitive  types 
# type() : used to get type of the value.

x=10 
print(x)
print(type(x)) #<class 'int'>

y=10.5 
print(y)
print(type(y)) #<class 'float'>

z=3+4j
print(z)
print(type(z)) #<class 'complex'>

''' why in python i is not used complex numbers
    we know that python is used in IOT (Internet of things, Embedded)
    Electrical and Electronics 
    I = reserved current 
    I = current 
    Ac = Z = Impetendence => complex value -> j 
'''

is_married = True
print(is_married)
print(type(is_married)) #<class 'bool'>

status = None 
print(status)
print(type(status)) #<class NoneType>

name = 'ravi' # single qoute
print(name)
print(type(name)) #<class str>

full_name = "Awnish Kumar Sharma" #double qoutes
print(full_name)
print(type(full_name)) #<class str>


s1 = """ This is a Triple double Qoute"""
s2 = ''' This is a Triple single qoute'''
print(s1)
print(type(s1))
print(s2)
print(type(s2))
