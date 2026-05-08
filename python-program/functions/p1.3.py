# In Python every python file itself is a module


import os
import sys 
import test

print("--------------------------This is code from p1.3.py-----------")
print('This is P1.3.py File')
print('value of name variable:',__name__)
print('value of file variable',os.path.basename(__file__))
print('value from argv:',sys.argv[0])
