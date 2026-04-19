# Collection datatypes : They are not primitive in nature.
# Collection datatypes are those datatypes those types which have can be used 
# to store mutliple values 

l = [10,20,30]
print(type(l))

colors = ['Blue','Yellow','Red']
print(colors)
print(type(colors))

mixed = [10,50.5,True,None,[10,20],'Awnish',30+2j]
print(mixed)
print(type(mixed))

t1 =(1,2,3,4)
print(t1)
print(type(t1)) # <class 'tuple'>

s = {10,10,20,20,30,30,50,50,50}
print(s) #uniques values 
print(type(s))

fs = frozenset(s)
print(fs)
print(type(fs))

d = {'name': 'Awnish','age':28}
print(d)
print(type(d))

numbers_list = range(1,10) #1,2,3,4,5,6,7,8,9 (1,n-1)
print(numbers_list)
print(type(numbers_list))

print(list(numbers_list))

numbers_list1 = range(1,10,2) # 1,3,5,7,9
print(list(numbers_list1))

