# How to take multiple argument in single line 
# Runtime argument

x,y,z = [int(x) for x in input("Enter the value:").split()]
print('sum:',x+y+z)

#input("Enter the value:") : '10 20'  
#x = '10 20'.split() 
#['10','20'] 
#[10,20]  # list comprehension
#x,y = [10,20]  # list unpacking