#!usr/bin/python3
"""filter"""
nums = [1, 3, 9, 7, 6, 4, 8, 12, 17]
"""
#Syntax for filter => filter(function, iterable)

def odd_nums(n):
    if n % 2 != 0:
        return n

odds = list(filter(odd_nums, nums))
print(odds)"""

# filter(odd_nums, nums): This returns a filter object and should be changed into a list function when printing

"""Using lambda and filter"""
odds = list(filter(lambda n: n % 2 != 0, nums))
even = list(filter(lambda n: n % 2 == 0, nums))
print(odds)
print(even)

"""The codes for odds and even can be written in a single line as:"""
print(list(filter(lambda n: n % 2 != 0, nums)))
print(list(filter(lambda n: n % 2 == 0, nums)))
