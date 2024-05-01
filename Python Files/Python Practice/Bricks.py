#This will print 3x3 bricks
for i in range(3):
    for j in range(3):
        print("#", end="")
    print()  

print("=======")  

#This is another method
for i in range(3):
    print("#" * 3)
