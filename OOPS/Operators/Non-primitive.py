#Non Primitive Data Type
# List  []      Touple()         Set{}      Dictionary  {}

mylist = ["apple", "banana", "cherry","ajay","Chaitu","Sattu"]

print("\n",mylist)
print("First Element of list is : ",mylist[1])
print("Last Element of List is : ",mylist[-1])
print("Print In between Data 2 - 5 ",mylist[2:5])
print("Print data in between with negative indexing ",mylist[-4:-2])

mylist.append("Dadu")
mylist.append("ajay")
print(mylist)
mylist.remove("Dadu")
mylist.remove("ajay")
print(mylist)
print(mylist)