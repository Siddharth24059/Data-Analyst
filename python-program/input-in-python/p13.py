# wap in python to show the compile time argument 
# how can we sum the multiple arguments.
import sys 

total = 0
for i in range(1,len(sys.argv)):
    total = total + int(sys.argv[i])

print('Total:',total)

