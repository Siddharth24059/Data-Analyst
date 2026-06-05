# wap in python to show the alternate of the print
# in python we have a module named "sys" which is has function 
# write function using which we can implement print

import sys 

print("Hello world this is print 1")
print("Hello world this is print 2")
# Note : sys has 3 objects 
# standard Input :stdin
# standard output :stdout
# standard error  :stderr

sys.stdout.write("Print without print 1 \n")
sys.stdout.write("Print without print 2")
