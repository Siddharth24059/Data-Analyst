# Type Hinting 
# Even thougt we donot declare type in python , # but after 3.5 version
# python allows you declare type 
# mypy : static type checker for python
# for we use package called as pydantic : data validation and settings management using python type annotations


#x= 'Siddharth' # type of x is str
# var_name : data_type = value


# x : int = 'Siddharth'
# print(x)
# print(type(x))

# # x=10
# # print(x)
# # print(type(x))

# y:int=10 # type -> int 
# print(y)
# print(type(y))

from typing import Union

z:Union[str,int,float] = 3.14
print(z)
print(type(z))


