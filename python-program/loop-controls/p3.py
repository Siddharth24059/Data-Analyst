# working with range : list of Sequences 
# range(start,end,step)

#start : Starting point of the sequence (inclusive) : default value is 0
#end : Ending point of the sequence (exclusive) : n-1
#step : Step size of the sequence : default value is 1

print(range(5)) # 0 to 5
print(range(1,5)) # 1 to 5
print(range(1,5,2))

#Range start to end-1

print(list(range(5)))
print(list(range(1,5)))
print(list(range(1,5,2)))


# dynamic Range
n = int(input('Enter the no:'))
print(list(range(1,n)))

