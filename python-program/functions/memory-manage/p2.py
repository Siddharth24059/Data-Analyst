
print("===============Code started executing==========")

def test():
    print("Test fn is execution..")
    x = 10 # local Variable
    y=20
    print(f'Stack Frame is Created where x = {x}  is local variable at x=id = {id(x)}')
    print('local scope memory=',locals())

print("===============Code still executing==========")
test()

print('Globals scope memory=',locals())