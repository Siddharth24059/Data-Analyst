import time
# sleep : in order to add delay.
# This delay on Horizontal is called snortting Effect.
# wap in python to fix snortting effect.

#total delay : time*no of iteration = total delay in second.
# delay:10 sec

# How to compute the delay in the execution of the code.
# can we start printing without flush without snorting fix
# No Buffering

import sys

print('========= Timer started======')
start_time = time.time()
print('start time:',start_time)

for i in range(10):
    print('Hello => ',i,end='')
    sys.stdout.flush()
    time.sleep(2)

print()
print('========= Timer ended======')

end_time = time.time()
print('End Time',end_time)
delay = round(end_time - start_time,2)
print('Total delay in Seconds:',delay)
