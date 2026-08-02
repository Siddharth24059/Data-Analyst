# Types of loops 
# Nested loops : one loop inside another loop

i=1 # start counter
while(i<=5):
    print(f'Outer start i = {i}')
    j=1
    while(j<=3):
        print(f'Inner loop j={j}')
        j=j+1
    print(f'Outer End i = {i}')
    i=i+1