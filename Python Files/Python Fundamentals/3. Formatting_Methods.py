#FORMATTING STRINGS
# Using f{}
"""
item = "milk" 
quantity = 5 
cost = 35.50 
price = cost * quantity

print(f"The product {item} costs {cost *  quantity} pesos.") 

sampleText = f"The item that costs {cost  * quantity} pesos is the product {item}." 
print(sampleText)
"""

# Using of format()
"""
name = "John"
food = "Rice"
game = "Chess"

formatText= "My name is {} i love {} and playing {}"
sampleText1a = formatText.format(name, food,  game)
print(sampleText1a)
"""


# Using format() while manipulating order
"""
name = "John"
food = "Rice"
game = "Chess"

formatText = "My name is {2} i love {1} and playing {0}"
sampleText2a = formatText.format(name, food,  game)
print(sampleText2a)
"""

# Using format() while assigning new values
"""
formatText = "My name is {newname} i love {newfood} and playing {newgame}"
sampleText3a =  formatText.format(newname="Mike", newfood="burger", newgame="volleyball")
print(sampleText3a)
"""

# Using format() to specify decimal places of a float
"""
x = 123456
print('The number is {:,.2f}'.format(x))  
"""

# Using format() to convert into percentage
"""
x = 0.5
print('{:.0%}'.format(x))  # 50%
"""

# Using %
"""
qty = 2
item = "milk" 
cost = 35.575

print("The product %s with item no. %d costs %.2f" %(item, qty, cost))

sampleText4 = "The product %s that costs %.2f is the item no. %d " %(item, cost, qty)
print(sampleText4) 
"""


#FORMATTING NUMBERS
# round() - used to round the floating-point number
# syntax: round(variable, decimal places)
"""
x = 3.14159
print(round(x, 2)) 
"""

# eval() - evaluates a math expression in a form of a string
"""
print(eval("5 + 5"))
"""

import math
# ceil() - round a floating-point number up to the nearest integer
"""
x = 2.59
print(math.ceil(x))  
"""

# floor() - round a floating-point number down to the nearest integer
"""
x = 2.59
print(math.floor(x))  
"""

# pow() - raise a number to a specified power
# syntax: pow(base, exponent)
"""
print(pow(2, 3)) 
"""