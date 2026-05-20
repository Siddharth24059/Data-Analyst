# wap in python to generate the dictionary using 2 list


l_keys = ['a','b','c','d','e','f','g']
l_values=  [1,2,3,4,50,100,150]


d = {l_keys[i]:l_values[i] for i in range(0,len(l_keys))}

print(d)