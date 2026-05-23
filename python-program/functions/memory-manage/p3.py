# Memory Management by gc 
import gc

def temp():
    print('Temp fn is executing..')
    print("Stack Frame is created")
    x = [1, 2, 3, 4]
    y = 10
    z = 100

    print('id of x =', id(x))
    print('id of y =', id(y))
    print('id of z =', id(z))
    print("Objects before GC inside function:", len(gc.get_objects()))
    print("GC collected inside function:", gc.collect())
    print("Objects after GC inside function:", len(gc.get_objects()))
    print('=================================================')

print("Before function call:", len(gc.get_objects()))
temp()
print("After function call (before GC):", len(gc.get_objects()))
print("GC collected after function:", gc.collect())
print("After function call (after GC):", len(gc.get_objects()))