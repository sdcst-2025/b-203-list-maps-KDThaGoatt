"""
### Assignment 1
Convert to Fahrenheit
Given a list of numbers that are in degrees Celsius, create a map() that returns a list of all the numbers converted to degrees Fahrenheight
"""

def degFaren(C):
    F = (C * (9 / 5)) + 32
    return F

data = [0, 10, 20.1, 34.5]
fahrenheit = map(degFaren, data)
print(list(fahrenheit))

# expected output:  [32.0, 50.0, 68.18, 94.1]