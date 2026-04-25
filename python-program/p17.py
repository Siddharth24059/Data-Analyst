# Type of Type casting 
# 1 : implicit -> Automatic 
# 2 : Explicit -> Forcefully.

#implicit Type work on the basis of mathematical typecasting 
'''
int + int = int 
int - int = int 
int * int = int 
int / int = float # int / int = float - float division
int // int = int 
'''

x=3 
y=2
print(x+y) # 5
print(x-y) # 1
print(x*y) # 6
print(x//y) # 1  # int-division
print(x/y) # 1.5  # float-division --> example -> implicit Type conversion 

x=3 # ---> 3.0 
y=2.5
print(x+y)  # float 
print(x-y)  # float 
print(x*y)  # float 
print(x//y) # float ----> float/float -> float
print(x/y)  # float => if int or float -> float 


# 2.3 --> ciel --> 3
# 2.3 --> floor --> 2 
# 2.0 --> ciel or floor --> True 
