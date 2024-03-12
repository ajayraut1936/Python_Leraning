# Half Pyramid of Stars
# *
# * *
# *  *  *
# *  *  *  *
# *  *  *  *  *

for i in range(0,4):
    # print("*",end=(" "))
    for j in range(0,i+1):
        print("*",end=" ")
    print("")

# *  *  *  *  *
# *  *  *  *
# *  *  *
# *  *
# *
for i in range(5):
    # print("*",end=(" "))
    for j in range(i,5):
        print("* ",end=" ")
    print()

print("\n\n\n")
for i in range(5):
    print()
    for j in range(-5,-i):
        print("",end="")
    for s in range(i+1):
        print("*   ", end="")