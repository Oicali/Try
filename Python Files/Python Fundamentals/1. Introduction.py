#PRINTING A TEXT
'''
print("Hello World!")
'''


#ASSIGNING VARIABLES
# int or integer : whole number, positive or negative, without decimals, of unlimited length.
# float or floating point number : number, positive or negative, containing one or more decimals.
# strings : Alphanumeric and surrounded by either single quotation marks, or double quotation marks.
# boolean : evaluated with either of the values True or False
'''
x = 5
name = "John Doe"
price = 88.75
married=True

print(x)
print(name)
print(price)
print(not married)
print(married)
'''


#PRINTING MULTI-LINE STRING FOR A STRING
'''
a = """
Hello World, 
Hello Python! 
""" 
print(a) 
'''


#GETTING THE DATA TYPE OF A VARIABLE
# You can get the data type of any object by using the type() function
'''
x = 5
name = "John Doe"
price = 88.75
married=True

print(type(x))
print(type(name))
print(type(price))
print(type(married))
'''


#DYNAMIC-TYPING
# A variable is determined only during runtime
'''
x = 5
x = "John Doe" 
print(x)
'''


#TYPECASTING
# Changing the data type of an object 
"""
x = 7 
x = float(7)
print(x)
"""


#CONCATENATING
# Converting int into string is important when concatenating string with an int
# Use the function str()
"""
x = 7
print("You number is " + str(x))
"""


#ASSIGNING MULTIPLE VALUES TO SEVERAL VARIABLES 
"""
x, y, z = "red", "white", "yellow" 
print(x)
print(y)
print(z)
"""


#ASSIGNING A VALUE TO MULTIPLE VARIABLES
"""
x = y = z = 2  
print("X = " + str(x))
print("Y = " + str(y))
print("Z = " + str(z))
"""


#INPUT AND OUTPUT VARIABLES
# Use the function input()
"""
name = input("Enter Full Name: ") 
email = input("Enter Email: ") 
print("Name: " + name) #the use of '+' for concatenation print("Email: " + email)
print("Email: " + email)
"""


#ARITHMETIC OPERATIONS
# Addition : [+]
# Substraction : [-]
# Multiplication : [*]
# Division : [/]
# Exponentiation : [**]
# Modulus : [%]
# Floor Division : [//]
"""
x = 10 
y = 10
print(int(x) + int(y)) #arithmetic addition 
print(x+y) 
print(float(x) + float(y))
"""


#COMMENTS 
# For explaining a code or documentation and skipping codes during testing 
# [#] is used for single line comment 
# ["""   """] and [''' '''] are used for multi-line comment 


#ESCAPE CHARACTERS
# \n - newline
# \t - tab
# \r - carriage return
# \b - backspace
# \' - single quote
# \\ - backslash
"""
print('John said "I don\'t like vegetables"')
print("This next text will move to the \nnext  line")
"""