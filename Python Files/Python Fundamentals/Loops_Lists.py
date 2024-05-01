#WHILE LOOP
#we can exit the loop even if while condition is  still true
#a=a+1
"""
a = 1
while a < 6: 
    print(a)
    a+=1   
"""


#the loop body are the statements being repeated
'''
a = 1 

while a < 6:  
    print(a)
  
    if a==4:
        break
    a+=1
'''


#The continue statement in Python returns the control to the beginning of the while loop. 
#The continue statement rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop.
'''
var = 7

while var > 0: #dont forget the colon when using while and for loops
  var -= 1     #var = var - 1
  
  if var == 5:
      continue
    
  print ('Current variable value :', var)
  
print ("Good bye!")
'''


#ELSE STATEMENT IN WHILE LOOPS
#The else part is executed if the condition in the while loop evaluates to FALSE
'''
a = 1

while a < 6: 
  print(a)
  a += 1
  
else:
   print("a is no longer less than 6")

'''


#FOR LOOP
#Generate numbers between 0 to 9
#range is a function that returns a sequence of numbers starting from 0 (by default), increments by 1 (by default), and stops before a specified number 
'''
for ctr in range(10):
    print(ctr)
'''


#Syntax: range(start, stop, step) 
#0 - start value, 10 - stop value, 2 - increment value
#The loop will execute if a < stop value
'''
for a in range (0,10,2):     
 print(a)
'''


#10 - start value, 0 - stop value, -2 - decrement value
#The loop will execute if a > stop value
'''
for a in range (10,0,-2):     
 print(a)
'''


#looping through a string
'''
for x in "bananapple":
 print(x) 
'''


#This is a For loop that counts i using the list
"""
for i in [0, 1, 2]:
    print("Hello World")
    print(i)
"""


#This another example that counts i. It sets the count from left to right (1-3)
"""
for i in [1, 2, 3]:
    print(f"Hi {i}")
"""


#break, continue, and pass can also be used with for loops 
'''
for x in "banana": 
  if x=='b': 
    #break
    #pass
    continue
    
  print(x) 
'''


'''
#ACTIVITY 2
#Break time
'''
'''
#arithmetic operators + - / * %
a=10

if a%2 == 0:        # percent here is a modulo operator
 print("a is divisible by 2") 

c = 11%2
print(c)

print('-'*100)
print("-"*20)  #prints - 20 times
'''

#Lists
#looping through a list

#Lists are used instead to store multiple items in a single variable
'''
#access of list elements
numbers = [1, 2, 3, 4, 5] 
food = ["cake", "burger", "fries"] 
print(numbers[0]) # 1 
print(food[1])  #burger
print(type(food))  #list
'''
'''
#From python's perspective, lists are objects with  data type
food = ["cake", "burger", "fries"] 
print(type(food)) 
'''
'''
#changing/assigning elements
food = ["cake", "burger", "fries", "cake"]
food[1] = "rice"
print(food) 
'''
'''
#List elements are ordered, changeable, and allow duplicates
#Python allows negative indexing i.e., -1 for the last element,
# -2 for the second to the last, etc.

food = ["cake", "burger", "fries", "spagetti"]
print(food[-2])     #this access the second to the last element of the list
'''
'''
#Python list may contain different types  
mixed_list = ["Mike", 1, 2, "John", 2.5, True]
print(mixed_list)
print(type(mixed_list[0]))

for x in mixed_list:
    print(x)
'''
'''
#looping through list elements
names = ["Mike", "Ana", "Jun"] 
for name in names: 
    print(name)
'''

#LIST HANDLING METHODS
'''
#len()
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print("Current fruit :", fruits[index])
'''
'''
#adding elements to a list
numList = [1, 2, 3, 4, 5] 
numList.append(99) #adds at the end of the list
print(numList)
'''
'''
male = ['John','Mike'] 
male.insert(1,"Jake") #inserts at a specified  index position
print(male) 
'''
'''
#removing elements
male = ['John','Mike','Jake'] 
male.remove("Jake") #removes specified item
print(male)
'''
'''
#pop()
male = ['John','Mike','Jake'] 
male.pop(1) #removes item on specified index
print(male) 
#if no specified index, removes last item 
'''
'''
#the use of del
male = ['John','Mike','Jake'] 
del male[1] #removes item on specified index
print(male)
'''

#deleting the list
male = ['John', 'Mike', 'Jake']
del male  #removes male completely from memory
#print(male)
#upon printing, a not defined error is encountered
'''
#clear list elements
male = ['John','Mike','Jake']
print(male)
male.clear() #male becomes an empty list
print(male)
'''
'''
#arranging/sorting elements
numList = [20, 2, 33, 42, 25] 
numList.sort() #by default ascending 
print(numList)

numList.sort(reverse=True)  #sets order to descending
print(numList) 

fruitList = ["orange", "mango", "kiwi", "banana"]
fruitList.sort() #by default ascending  alphanumerical 
print(fruitList) 
'''
'''
#reverse order of elements
numList = [20, 2, 33, 42, 25] 
numList.reverse() 
print(numList) 
'''
'''
#count()
numList = [25, 2, 33, 42, 25] 
counter = numList.count(42)  #counts the instances of 42 in the list numlist
print(counter) 

fruitList = ["banana", "banana", "apple", "cherry"]
counter2 = fruitList.count("banana")
print(counter2)
'''
'''
#index()
numList = [11, 2, 33, 42, 25] 
indexPosition = numList.index(42)
print(indexPosition)
'''
'''
#copying lists
fruits = ["apple", "banana", "cherry"]
mylist = fruits.copy()  
print(mylist) 
'''
'''
#list = fruits
fruits = ["apple", "banana", "cherry"]
mylist = list(fruits) #use of list()
print(mylist)
'''
'''
#combining lists/iterables
male = ['Bien','John'] 
female = ['Jayde','Ana'] 
mixed = male + female #use of + operator
print(mixed)
'''
'''
male = ['Bien','John']
print(male)

female = ['Jayde','Ana'] 
male.extend(female) #appends the elements of  female at the end of male 
print(male) 
print(female)
'''
'''
#appending from a list using for loop
male = ['Bien','John'] 
female = ['Jayde','Ana'] 
for x in female: 
    male.append(x)
print(male) 
'''

#List comprehension techniques
#shorthand syntax of creating lists from existing  ones
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

#Syntax:
#newlist = [<expression> for <item> in <iterable>  if <condition> == True]
#fruits = ["apple", "banana", "cherry", "kiwi",  "mango"]
#newlist = [x for x in fruits if "a" in x] #newlist = [x for x in fruits] #no condition #newlist = [x for x in fruits if x != "mango"]  #except mango
#print(newlist)
