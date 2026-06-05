# wap in python to difference B./w print and stdout.write()

import sys 
import time 

for i in range(5):
    print("Hello=",i)
    time.sleep(1)


for i in range(5):
    print("Hello=",i,end="",flush=True)
    time.sleep(1)


