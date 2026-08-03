# module aliasing concept is applied on the import states or from .. import statement 
# member are any classname ,objectname,function,variable defined with9n the module
#import using from
#with reference
import math as m 
# module name or its alias will act as refrence

print(m.pi)
print(m.sqrt(25))

#without Reference
from math import sqrt as sq,pow as pw
#print(sqrt(16))
#print(pw(2,3)) 

print(sq(16))
print(pw(2,3))