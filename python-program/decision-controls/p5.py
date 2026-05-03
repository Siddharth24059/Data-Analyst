
# we have something other then if which is called elif 
# elif is short form of else+if 

#Grades
# A -> 90 to 100 (inclusive and exclusive)
# B -> 80 to 89 
# C -> 70 to 79
# D -> 60 to 69
# E -> 50 to 59
# Fail < 50 

marks = eval(input('Enter the marks:'))

if marks>=90 and marks<=100:
    print('Grade A')
elif marks>=80 and marks<=89:
    print('Grade B')
elif marks>=70 and marks<=79:
    print('Grade C')
elif marks>=60 and marks<=69:
    print('Grace D')
elif marks>=50 and marks<=59:
    print('Grade E')
else:
    print('Failed')