#wap in python who to take input 
# Rmeove the backslash \n we can use strip,rstrip,replace("\n","")

import sys

sys.stdout.write("Enter the value:")
sys.stdout.flush()
name = sys.stdin.readline()  #awnish\n
print(repr(name))
new_name = name.strip()
print(new_name)
print(repr(new_name))