'''
### Assignment 3
Remove leading or trailing whitespace
Given a list of words, remove any spaces at the beginning or end of the word
'''

def removeSpace(word):
    noSpace = str.strip(word)
    return noSpace

data = ['  apple', 'banana ', '  mango ', 'grape']
noSpaces = map(removeSpace, data)
print(list(noSpaces))
# expected output: ['apple', 'banana', 'mango', 'grape']
# HINT: use the str.strip() method to remove whitespace from the beginning and end of a string

