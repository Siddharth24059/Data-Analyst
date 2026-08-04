# Example of Special Operators :-=
# isinstance : it tell wheather a Percular element is an Object that Class  


# class is blueprint or template of an Object 
# every Object is an instance of a class


name = 'Awnish'
print(type(name))
print(isinstance(name,str)) #true

x = 10 
print('type of x:',type(x)) #int
print(isinstance(x,str)) #false
print(isinstance(x,int)) #true

d = {'age':20,'name':'Ravi'}
print(d)
print(type(d))
print(isinstance(d,str)) #false
print(isinstance(d,dict)) #true