#STRING MANIPULATION FUNCTIONS

#UPPERCASE STRINGS
# upper() - Converts a string into upper case
'''
s = "Hello World!"
print(s.upper())
'''


#LOWERCASE STRINGS
# lower() - Converts a string into lower case
'''
s = "Hello World!"
print(s.lower())
'''


#CAPITALIZED STRINGS
# capitalize() - Converts the first character to uppercase
'''
s = "manila city government philippines"
print(s.capitalize())
'''


#TITLE STRINGS
# title() - Converts the first character of each word to uppercase
"""
string = "cavite, philippines"
print (string.title())
"""

#SWAPCASE STRINGS
# swapcase() - Changes the lowercase characters into uppercase and vice versa
"""
string = "bACOOR City"
print(string.swapcase())
"""


#REPLACE IN A STRING
# replace() - Returns a string where a specified value is replaced with a specified value
# syntax: string.replace(oldvalue, newvalue,  count) 
"""
s = "I like playing basketball and basketball."
x = s.replace("basketball", "football")
print(x)
x1 = s.replace("basketball", "football",1)
print(x1)
"""


#COUNTING THROUGH THE STRING
# count() - count the number of occurrences of a specified substring within a string.
"""
word = 'Hello, World'
print(word.count('l'))
"""


#LENGTH OF A STRING
# len() - count characters in a string
'''
s = "Hello World!"
print(len(s))
'''


#SPLITTING STRINGS
# split() - Splits the string at the specified separator, and returns a list
# default separator is any whitespace 
# syntax: string.split(separator, maxsplit)
"""
print("Hello World".split())

sentence = 'The quick brown fox jumps over the lazy dog'
words = sentence.split()
print(words)

s1 = "Hello, my name is John, I am doing Python."
x = s1.split(",")
print(x)
print(type(x))
"""


#STRIP STRINGS
# strip() - removes whitespace at the start and end 
# lstrip() - removes leading characters (Left-strip)
# rstrip() - removes trailing characters (Right-strip)
"""
s = "    Hello, Python!     "
print(s.strip())
print(s.lstrip())
print(s.rstrip())
"""


#JOINING AND REVERSING STRINGS
# join() - join a list of strings into a single string
# reversed() function is used to reverse the string
"""
words = ['The', 'quick', 'brown', 'fox']
sentence = ' '.join(words)
print(sentence) 

print(' '.join(reversed(words)))
"""