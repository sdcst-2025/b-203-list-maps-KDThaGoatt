'''
### Assignment 4
Capitalize words
Given a list of words, make sure that the first letter is capitalized and the rest are lower case.
'''

def capWords(word):
    capitalized = str.capitalize(word)
    return capitalized

data = ['apple', 'BANANA', 'mango', 'GrapE']
caps = map(capWords, data)
print(list(caps))

# expected output: ['Apple', 'Banana', 'Mango', 'Grape']
# HINT: use the str.capitalize() method to capitalize the first letter of a string and make the rest lower case
