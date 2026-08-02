# Types of loops 
# Python two of loops 
# for loop 
# while
#

from time import sleep
'''
Syntax of while loop

counter = initial value
while condition:
    # body of the loop
    # update the counter

''' 

# we donot have do-while in python
i=1 # start counter
while(i<=5): # Falsey condition : when I is greater than 5 loop will stop
    print(f'Hello = {i}')
    i+=1 # update the counter : incrementing the counter by 1
    sleep(1)

    # Infinite loop : loop which runs forever
    # i = 1 will always be less than 5
    # to avoid infinite loop we need to update the counter
