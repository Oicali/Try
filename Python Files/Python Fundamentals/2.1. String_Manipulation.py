#ACCESS INDEX OF STRINGS
# The index of the first character in a string is 0, and the index of the last character is -1
"""
word = 'Hello'
print(word[0]) 
print(word[-1])
"""


#SLICING STRINGS
# Returns a range of characters by specifying the slice
# Negative indexing, starts the slice from the very end
'''
word = "Hello, World!" 
print(word[2:5])  
print(word[-5:-2])
'''


#REPEATING STRINGS
# Repeat a string multiple times using the [*]
"""
text = 'Hello '
print(text * 3)

print("HA" * 4)
"""


#CHECKING STRINGS
# Returns True or False 
# Check if a string is found
"""
word = 'Hello'
print('H' in word)  
"""

# startswith() - Check if a string starts with
"""
word = "hello world"
print(word.startswith("h"))
"""

# endswith()- Check if a string ends with
"""
word = "hello world"
print(word.endswith("D"))
"""

# isalpha() - Check if all char in the string are alphabetic
"""
word = "email123"
print(word.isalpha())
"""

# isalnum() - Check if all char are alphanumeric 
"""
word = "email123"
print(word.isalnum())
"""

# isdigit() - Test if string contains digits
"""
word = "123"
print(word.isdigit())
"""

# istitle() - Test if string contains title words
"""
word = "Bacoor city"
print(word.istitle())
"""

# isupper() - Test if string contains upper case
"""
word = "HELLO WORLD"
print(word.isupper())
"""

# islower() - Test if string contains lower case
"""
word = "city"
print(word.islower())
"""

# isspace() - Test if string contains spaces only
""""
word = " "
print(word.isspace())
"""


#SEARCHING THROUGH STRING
# find() - method returns the index of the first occurrence of the substring in the string
# Returns -1 if the substring is not found.
"""
word = 'Hello'
print(word.find('l'))  
"""

# index() method - returns the position at the first occurrence of the specified value
"""
fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
"""

# rfind() method - finds the last occurrence of the specified value
"""
word = 'Hello Hi Hello'
print(word.rfind('l'))  
"""