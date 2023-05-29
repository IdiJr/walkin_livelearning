#!/usr/bin/python3

def square():
    squares = []
    for i in range(0, 10):
        if i == 3:
            continue
        squares.append(i**2)
    return squares

print(square())
print([i**2 for i in range(0, 10) if i !=3])
