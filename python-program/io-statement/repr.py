# repr refers to representation it is used to represent in its internal
# repr stores escape character sequence


import datetime

name = "Rahul\n"
print(name)

name = "Rahul\n"
print(repr(name))


# used to show the hidden characters in the string 

print("Hello \t world")
print(repr("Hello \t world"))


# repr can be used to override custom class.
class Student():
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return self.name

s = Student('Rahul')

print(s)
print(repr(s))

# repr can be used with internal objects 
now = datetime.datetime.now()
print(now)
print(repr(now))