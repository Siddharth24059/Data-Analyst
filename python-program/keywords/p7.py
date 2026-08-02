# wap in python to show if the given keyword is hard keyword or soft

import keyword as kw

def isSoftKeyword(keyword):
    return kw.issoftkeyword(keyword)

# Hard Keyword 

print('is isSoftKeyword :',isSoftKeyword('True'))
print('is isSoftKeyword :',isSoftKeyword('as'))
print('is isSoftKeyword :',isSoftKeyword('import'))
print('is isSoftKeyword :',isSoftKeyword('if'))
print('is isSoftKeyword :',isSoftKeyword('else'))
# soft Keyword 
print('is isSoftKeyword :',isSoftKeyword('match'))
print('is isSoftKeyword :',isSoftKeyword('type'))
print('is isSoftKeyword :',isSoftKeyword('case'))
print('is isSoftKeyword :',isSoftKeyword('_'))



