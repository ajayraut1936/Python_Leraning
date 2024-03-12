# #  Collection
# '''
#                 Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# 1]List is a collection which is ordered and changeable. Allows duplicate members.
# 2]Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# 3]Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# 4]Dictionary is a collection which is ordered** and changeable. No duplicate members.
# '''

# List_items=['Ajay','Chaitu',"Raut",50]
# print("This is List from collection :",List_items)

# print("Access items by Index 1:",List_items[1])
# print("Access items by Index -2:",List_items[2])
# print("Access items by Index [1:]:",List_items[1:])
# print("Access items by Index [2:3]:",List_items[2:3])

# #Chnage values by Index

# List_items[2]="Phadtare"
# print("Updated Values for 2nd position : ",List_items)

# #Insert values from List

# List_items.insert(0,'Fuck')
# print("After insert values : ",List_items)

# #Remove Values from list

# List_items.remove('Fuck')
# print("After removing values are : ",List_items)

# #Remove Specific Index List value
# List_items.pop(1)
# print("After removing index 1 by POP(index)", List_items)

# #remove the alst element from the list
# List_items.pop()
# print("After pop without values remove last value, ",List_items)
# #Extend List

# List_2=['fuck','chaitu','mc','bc']
# List_items.extend(List_2)
# print("After Extending the List is : ",List_items)

# del List_2
# print("Delete List 2")

# #cleare the list

# List_items.clear()
# print("CLeare all the values from list :>",List_items)




# #--------[ Looping In List ]----------------------------------------------------------

# List_3=['sattu','sarvesh','swarup','chaitu']
# print('\n\nThs for loop Iteration of List :"')
# for item in List_3:
#     print(item)


# #Loop through Iteration
# for i in range(len(List_3)):
#     print("The second no values is : ",List_3[i])





# #Sort the String in Python

# List_3.sort()
# print("After sorting: ",List_3)

# #Reverse Sort

# List_3.sort(reverse=True)
# print("After reverse Sorting: ",List_3)


# '''
# append()	        Adds an element at the end of the list
# clear()	            Removes all the elements from the list
# copy()	            Returns a copy of the list
# count()	            Returns the number of elements with the specified value
# extend()	        Add the elements of a list (or any iterable), to the end of the current list
# index()	            Returns the index of the first element with the specified value
# insert()	        Adds an element at the specified position
# pop()	            Removes the element at the specified position
# remove()	        Removes the item with the specified value
# reverse()	        Reverses the order of the list
# sort()	            Sorts the list



# '''

# List_items=[34,343,34,24,4,2,123,1,34,2,50]

# print(List_items)
# sorted_list= List_items.sort()

# print(List_items)
# List_items.sort(reverse=True)
# print(List_items)

# string= "This is my name over the ajay top of the"
# print(string)
# string1=string.split()
# print(string1)
# string1.sort(key=len,reverse=True)
# print(string1)








#######  List Functions

aaaa = "this is MY personal id and my id has good Count"

print(aaaa.capitalize())   # Convert first letter of sentace 
print(aaaa.title())        # Convert all words first letter in capital
print(aaaa.lower())        # convert whole string to lower
print(aaaa.upper())        # COnvert into upper case
print(aaaa.casefold())     # conver whole into lower case stronger than lower()
print(aaaa.index("id"))    # Return first occurence of substring in main string  from start of the string
print(aaaa.rindex("id"))   ## Return first occurence of substring in main string from end of the string 
print(aaaa.count("id"))    # retunr the total count od the substring in the main string 
print(aaaa.find("id"))     # return the first occurence of the string in main string
print(aaaa.rfind("id"))    # return the first occurence of the string in main string from end of the string
print(aaaa.split(" "))     # splite the string based upon the values
print(aaaa.partition("id")) # partation is done by name of the usbstring 
print(aaaa.strip())        # Remove the whitespace from the string 
# print(aaaa.center(12,"----"))
print(aaaa.isalnum())      # Return T if check string is alpha + numeric or not 
print(aaaa.isdigit())       # return true if it is digit 
print(aaaa.islower())       # to check if it is in lower case or not 
print(aaaa.isupper())      # check if string is in upper case
print(aaaa.istitle())     # is it is title or not 
print(aaaa.isspace())     # is string is in space or not





#########  List Functions 
# ['this', 'is', 'MY', 'personal', 'id', 'and', 'my', 'id', 'has', 'good', 'Count']

lst = list(aaaa.split())
print(lst)

print(len(lst))        #print the size of the list \
print(lst[:])          # Print all the element of the string 
print(lst[:3])         # print 0 to 3rd element of the string 
print(lst[1:4])        # print bet 1:4 
print(lst[-1])         # return first vlues from the last 
print(lst[::-1])       # reverse the string 
print(lst[-4:-1])     # print last 1 to 4 the elemnt from last 

lst[0] = "Ajay"
print(lst)
lst[0:2] = {"Ajay" ,"Chaitu"}
print(lst)

# Interting 
lst[0] = "AjayChaitu"
lst.insert(len(lst),"ChaituAjay")
print(lst)

# append 
lst.append("Fuck You append")
print(lst)

print(f"This is fucking {"name"}")


name_lst = ["Vijay", "Vickey"]
tup = ("Item_1", 0.5, name_lst)
name_lst.append("Vishal")
print(tup)


# elements = (10, 20, 30, 40, 50, 60, 70, 80)
# print(elements[2:5], elements[:4], elements[3:100])




dic = {"name":"Ajay","sname":"Raut","Age":25}
print(dic)
print(type(dic))
print(len(dic))      # print the size of the dic 
print(dic.keys())    # print keys of the dic 
print(dic.values())   # print the link of the values
print(dic.items())    # print items from dc 

print(dic["name"])    #acess the value by name
print(dic.get("name"))   # access the value by index name

dic["name"] = "Chaitu"
print(dic)

dic.update({"addr":"katrj"})
print(dic)

# dic.pop("addr")
# print(dic)

# del dic["Age"]
# print(dic)


for i in dic:
    print(i,end="  ")
    print(dic[i])

for i in dic.values():
    print(i)

string = "Ajay savata raut"
dic11={}
for i in string:

    # print(i)
    if i in dic11:
        dic11[i]+=1
    else:

        dic11[i]=1

print(dic11)


# initializing string
test_str = "GeeksforGeeks"
 
# using naive method to get count
# of each element in string
all_freq = {}
 
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
 
# printing result
print("Count of all characters in GeeksforGeeks is :\n "
      + str(all_freq))