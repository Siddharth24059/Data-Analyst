#  make a cube list  odd numbers from  1 to 100 by using list comprehension



l =[i*i*i for i in range (1,101) if i%2==1]
print('list of cubes of odd numbers:',l)