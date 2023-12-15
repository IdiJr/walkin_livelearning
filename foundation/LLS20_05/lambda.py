#!/usr/bin/python3

def maximum(a, b):
    if a > b:
        return a
    return b

print(maximum(12, 7)) # answer should be 12.

#lambda arguments: expression
largest = lambda a, b: a if a > b else b

print(largest(12, 3)) # aswer should be 12
print(largest(1, 5)) # answer should be 5
