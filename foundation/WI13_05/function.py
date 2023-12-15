#!usr/bin/python3
"""position arguments: in this type, the inputs are entered exactly as the variables are declared"""
def profile(name, age, gender):
    return(f"My name is {name} and I am {age} years old and I am a {gender}")
#print(profile("victor", 99))

"""Keyword / named argument: this type, we assign the variables with values directly so their positions can be cahnged"""
#print(profile(age=99, name="Victor"))

#Using both positional and keyword argument together
#print(profile(gender="Male", "Victor", 99)) #shouldn't run because positional argument comes after keyword argument
print(profile("Victor", 99, gender="Male"))
