#make a dynamic dictionary with all natural numbers with keys and cube 1 to 100


d = {i: i**3 for i in range(1, 101)  if i%2==1}

print(d)
