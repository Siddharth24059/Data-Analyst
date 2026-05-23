# use of function in python
from random import randint

def generateOTP():
    otp = ""        
    for i in range(4):
        otp += str(randint(0,9))
    return otp


# for i in range(10):
#     print(generateOTP())