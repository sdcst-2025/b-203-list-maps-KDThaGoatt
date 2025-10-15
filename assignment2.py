"""
### Assignment 2
Prime numbers
Given a list of numbers that are integers, create a map() that shows whether each of the numbers is a perfect square.
"""

import math

def isSquare(n):
    if math.sqrt(n) % 1 == 0:
        return True
    else:
        return False

data = [76, 56, 20, 77, 42, 81, 83, 47] 
squares = map(isSquare, data)
print(list(squares))


# expected output:  [False, False, False, False, False, True, False, False]

