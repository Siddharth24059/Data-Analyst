#for loop can also be used to Iterate through the collections using range function

name = 'Awnish'
       #A => 0, w => 1, n => 2, i => 3, s => 4, h => 5
print('length of name = ',len(name))

for i in range(0,len(name)): # 0 to 6 (0,1,2,3,4,5)
    print(f'i = {i} => {name[i]}')
