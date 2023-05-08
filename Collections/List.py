#  Collection
'''
                Python Collections (Arrays)
There are four collection data types in the Python programming language:

1]List is a collection which is ordered and changeable. Allows duplicate members.
2]Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
3]Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
4]Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''

List_items=['Ajay','Chaitu',"Raut",50]
print("This is List from collection :",List_items)

print("Access items by Index 1:",List_items[1])
print("Access items by Index -2:",List_items[2])
print("Access items by Index [1:]:",List_items[1:])
print("Access items by Index [2:3]:",List_items[2:3])

#Chnage values by Index

List_items[2]="Phadtare"
print("Updated Values for 2nd position : ",List_items)

#Insert values from List

List_items.insert(0,'Fuck')
print("After insert values : ",List_items)

#Remove Values from list

List_items.remove('Fuck')
print("After removing values are : ",List_items)

#Remove Specific Index List value
List_items.pop(1)
print("After removing index 1 by POP(index)", List_items)

#remove the alst element from the list
List_items.pop()
print("After pop without values remove last value, ",List_items)
#Extend List

List_2=['fuck','chaitu','mc','bc']
List_items.extend(List_2)
print("After Extending the List is : ",List_items)

del List_2
print("Delete List 2")

#cleare the list

List_items.clear()
print("CLeare all the values from list :>",List_items)




#--------[ Looping In List ]----------------------------------------------------------

List_3=['sattu','sarvesh','swarup','chaitu']
print('\n\nThs for loop Iteration of List :"')
for item in List_3:
    print(item)


#Loop through Iteration
for i in range(len(List_3)):
    print("The second no values is : ",List_3[i])





#Sort the String in Python

List_3.sort()
print("After sorting: ",List_3)

#Reverse Sort

List_3.sort(reverse=True)
print("After reverse Sorting: ",List_3)


'''
append()	        Adds an element at the end of the list
clear()	            Removes all the elements from the list
copy()	            Returns a copy of the list
count()	            Returns the number of elements with the specified value
extend()	        Add the elements of a list (or any iterable), to the end of the current list
index()	            Returns the index of the first element with the specified value
insert()	        Adds an element at the specified position
pop()	            Removes the element at the specified position
remove()	        Removes the item with the specified value
reverse()	        Reverses the order of the list
sort()	            Sorts the list
'''

