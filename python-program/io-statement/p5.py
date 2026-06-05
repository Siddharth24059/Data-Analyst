#wap in python to show case end and sep both 

print('siddharth','jaiswal',sep='-',end='!')
print('siddharth','jaiswal',end='!',sep='-')

# 'siddharth','jaiswal' : Position Argument : Position matters
print('siddharth','jaiswal',sep='-',end='!')
print('jaiswal','siddharth',end='!',sep='-')
#named arguments (sep,end,flush) : name argument : if we change the position output does not effect.