# nested Condition 

age = int(input('Enter the age:')) #20

if age>=18:
    print('You are eligible for Marriage')
    gender = input('Enter the gender:') #Male
    if gender.lower()== 'male':
        print('You can marry a girl')
    elif gender.lower() == 'female':
        print('You can marry a boy')
    else:
        print('You Belong to LGBTQA+')
else: 
    print('Baby, you are not eligible for Marriage')
