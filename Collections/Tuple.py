#  Collection
'''
                Python Collections (Arrays)
There are four collection data types in the Python programming language:

1]List is a collection which is ordered and changeable. Allows duplicate members.
2]Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
3]Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
4]Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''

tuplee=('ajay','savata','chaitrali','phadtare')
print(tuplee)

##  Aceesing tuple
print("Accesing tuple 1:",tuplee[1])
print("Accesing tuple [1:3]",tuplee[1:3])
print("Negative Index -2",tuplee[-2])

tuple12=list(tuplee)
print("Casting tuple to list :",tuple)

tuple1=tuple(tuple12)
print('Casting list to tuple :',tuple1)


'''

count()	        Returns the number of times a specified value occurs in a tuple
index()	        Searches the tuple for a specified value and returns the position of where it was found

'''

