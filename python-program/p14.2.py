

print(2+2*5/2) # 2+5.0 -> 7.0
print((2+2)*5/2) # 4*5/2 -> 20/2 -> 10.0

print(eval("2+2*5/2")) # 2+5.0 -> 7.0
print(eval("(2+2)*5/2")) # 4*5/2 -> 20/2 -> 10.0

exp = '2+2*5/2'
print(eval(exp))


exp1 = '2**2*5/2' # 2 to the power of 2 times 5 divided by 2
print(exp1) 
print(eval(exp1)) # 2^2*5/2 -> 4*5/2 -> 20/2 -> 10.0
