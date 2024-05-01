# Initializing a variable
name = "Jairus"
x = 5


# Printing the variable. The 2nd one is a Format string
print("Hello, " + name)
print(f"Hi, {name}")


# Printing the datatype
print(type(name))


# Printing a text
print("The answer is:", +x)


# Printing a random number from 1-10
import random

print(random.randrange(1, 10))


# Integers can add but not strings
c1 = 5 + 5j
c2 = 6 + 11j
print("Addition:", c1 + c2)


# Prints boolean expression
print(1 != 2)


# Prints the char in a array of string using index
a = "editor"
print(a[1])


# Inputs a value for a variable then prints random letter
letter = input("type a word: ")
print(str(letter[random.randrange(0, len(letter))]))


# Printing numerous times without using loops
print("!" * 4)
