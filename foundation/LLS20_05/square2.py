#!/usr/bin/python3

'''squares = []
for i in range(1, 10, 2):
    squares.append(i**2)
print(squares)'''
'''
#Syntax: map(functoin, iterable) #list, tuple

def square_fn(n): # n is the list
    return (n ** 2)

range(1, 10, 2) #lists from 1 to 10 skiping a number after the first

squares = map(square_fn, range(1, 10, 2)) # returns a map object
print(list(squares))'''

square_fn = lambda n: n ** 2 #This is a substitute for "def square_fn(n):\n return (n ** 2)

square = map(lambda n: n ** 2, range(1, 10, 2)) #This removes the need for naming the lambda definition
print(list(square))
