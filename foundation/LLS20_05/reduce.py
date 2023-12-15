a_list = [1, 2, 3, 5]

#add every element

"""def add_all(n):
    total = 0
    for i in n:
        total += i
        return total
print(add_all(a_list)) # Prints out the sum of all values in the list. """

"""Using Reduce"""
from functools import reduce

total = reduce(lambda x, y: x + y, a_list) # This is to add the items in the list, adds the first and second then adds the answer to the third till the last item.
print(total)
