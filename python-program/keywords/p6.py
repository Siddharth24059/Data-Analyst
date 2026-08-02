# wap in python to show if the given keyword is hard keyword or soft

import keyword as kw

def isHardKeyword(keyword):
    return kw.iskeyword(keyword)

# Hard Keyword 

print('is HardKeyword :',isHardKeyword('True'))
print('is HardKeyword :',isHardKeyword('as'))
print('is HardKeyword :',isHardKeyword('import'))
print('is HardKeyword :',isHardKeyword('if'))
print('is HardKeyword :',isHardKeyword('else'))
# soft Keyword 
print('is HardKeyword :',isHardKeyword('match'))
print('is HardKeyword :',isHardKeyword('type'))
print('is HardKeyword :',isHardKeyword('case'))
print('is HardKeyword :',isHardKeyword('_'))



