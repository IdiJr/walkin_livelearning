#!usr/bin/python3

"""
Args:
write a program that prints the maximum value of the variable number of arguments

"""
def maximum(*args):

    if len(args) == 0:
        return None
    else:
        max_value = args[0]
        for arg in args[1:]:
            if arg > max_value:
                max_value = arg
                return max_value

print(maximum())
print(maximum(2, 9, -100)) #retun 9
print(maximum(123, 34536, 466747, 4677)) #return 466747
