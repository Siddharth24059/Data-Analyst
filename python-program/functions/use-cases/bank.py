
from otp import generateOTP
from random import randint
print("============Awnish Finance Bank =============")

acc_name = input("Enter the Account Name:")
acc_dob = input("Enter the DOB:")
acc_gender = input("Enter the Gender:")
acc_father_name = input("Enter the Father Name:")
acc_mobile_no = input("Enter the Mobile No:")


print("=======Account Created Successfully==========")
print("Account No:","AFB-"+str(randint(111111111,999999999)))
print('Account Name:',acc_name)
print('Account DOB:',acc_dob)
print('Account Gender:',acc_gender)
print('Account Father Name:',acc_father_name)
print('Account Mobile No:',acc_mobile_no)

print("Account OTP:",generateOTP())
