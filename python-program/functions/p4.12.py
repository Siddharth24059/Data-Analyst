# Different Type of arguments in Python 
# varible length Named argument
import sys 
# **stars is used to pass variable length named argument in the form of dictionary

def add(**d): 
    print(d)
    print(type(d)) #<class 'dict'>
    print('keys',d.keys()) # keys = name,age,subject,marks,hostel
    #values = Awnish,50,physics,80,False
    print('values:',d.values())

def main():
    add(name='Awnish',age=50,marks=80,subject='physics',hostel=False) #length = 6 # position is not imported value is important

sys.exit(main())