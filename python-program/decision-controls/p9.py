# Make a Program for Odd and Even 
# No --> Divider --> Remainder 
# Remainder -> 0,1
# Remainder --> 0 ---> Even 
# Remainder ---> 1 ---> Odd

number = int(input('Enter the No:')) #11
output = ['Even','Odd']  #0,1
remainder = number % 2
print('No is ',output[remainder])







    