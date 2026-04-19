
#How to use print 
print('siddharth')
print("siddharth jaiswal")
x=10
print(x)

print('x=',x) #comman seperated values
print('x='+str(x)) # concatenation
print('x='+' '+str(x)) # concatenation

x=10
name = 'Ravi'
age = 20
print('x=',x,'name=',name,'age=',age)
print(f'x={x} name={name} age={age}') #format string or fstring
# f string is used as a prefix in any string.

# .format() string
print('x={x} name={name} age={age}'.format(x=x,name=name,age=age))
# we can use different variable

# without .format() 
print('x={a} name={b} age={c} in line 24')

# Example for the named Argument
print('x={a} name={b} age={c} in line 25'.format(a=10,b='Sunny',c=30))
print('x={a} name={b} age={c} in line 26'.format(b='Sunny',a=10,c=30)) # position changed.

print('x={a} name={b} age={c}'.format(a=x,b=name,c=age))

# Example of the Positional Argument
print('x={} name={} age={} in line 33'.format(x,name,age))
print('x={} name={} age={} in line 34'.format(age,name,x))
