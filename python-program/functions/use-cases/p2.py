
from random import randint
# print(randint(0,9)) # it will generate random number between 0 to 9

d1 = randint(0,9) # 4
d2 = randint(0,9) # 5
d3 = randint(0,9) # 9
d4 = randint(0,9) # 2

# print("============otp==================")
# # print('d1',d1)
# # print('d2',d2)
# # print('d3',d3)
# # print('d4',d4)


otp = str(d1)+str(d2)+str(d3)+str(d4)
print('otp:',otp)