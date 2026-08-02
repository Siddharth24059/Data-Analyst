# wap in python to show if the given keyword is hard keyword or soft, using custom function

import keyword as kw

def checkHardKeyword(keyword):
 return keyword in kw.kwlist


print('is hard keyword :',checkHardKeyword('True'))
print('is hard keyword :',checkHardKeyword('false'))  # false
print('is hard keyword :',checkHardKeyword('None'))
print('is hard keyword :',checkHardKeyword('if'))
print('is hard keyword :',checkHardKeyword('else'))
print('is hard keyword :',checkHardKeyword('as'))
print('is hard keyword :',checkHardKeyword('const'))  # false
print('is hard keyword :',checkHardKeyword('let'))    # false 
print('is hard keyword :',checkHardKeyword('var'))    # false 

