# memory management by gc
import gc

def temp():
    print('temp function is executing..')
    print("stack frame is created")
    x=[1,2,3,4]
    y=10
    z=100
    
    
    print('id of x =',id(x))
    print('id of y =',id(y))
    print('id of z =',id(z))
    print("object before gc inside function:", len (gc.get_objects()))
    print("gc collected inside function:",gc.collect())
    print("object after gc inside function:", len (gc.get_objects()))
    print('===================================================')
    
    
print("before function call:", len (gc.get_objects()))  
temp()
print("after function call:",len (gc.get_objects()))
print("gc collected after function call:",gc.collect())
print(" after function call:",len (gc.get_objects()))
