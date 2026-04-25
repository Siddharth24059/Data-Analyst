# eval(): derived from evaluation 
# eval() : used to dynamic type casting 
# eval() : can used to solve expression 

exp = '5*x**2+2*x+3' # 5x^2 + 2x + 3 find value of x at x=2
x = eval(input('Enter the value of x:')) #2 --> str 
 # 5x^2 + 2x + 3 find value of x at x=2
result = eval(exp)
print(f'The value Expression {exp} at x = {x}  is {result}')


