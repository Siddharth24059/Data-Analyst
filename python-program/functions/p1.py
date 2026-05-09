# memory management



print("=========code started executing=========")


def test():
    print("test function is execution..")
    x=10 # local variable
    y=20 # local variable
    print(f'stack frame is created where x={x} is local variable at x=id ={id(x)}')
    print('local scope memory',locals())
print("=========code still executing=========")
test()
print('globals scope memory',locals())