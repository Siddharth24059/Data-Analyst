# wap in python to difference B./w print and stdout.write()

import sys 
import time 

for i in range(5):
    sys.stdout.write("Hello from stdout")
    time.sleep(1)


for i in range(5):
    sys.stdout.write("Hello from stdout \n")
    time.sleep(1)




