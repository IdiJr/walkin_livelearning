#!usr/bin/python3
"""filter"""
nums = [1, 3, 9, 7, 6, 4, 8, 12, 17]

#Syntax for filter => filter(function, iterable)

def odd_nums(n):
    if n % 2 != 0:
        return n

odds = list(filter(odd_nums, nums))
print(odds)

filter(odd_nums, nums) # Returns a filter object and should be changed into a list funstion when printing
