#  Collection
'''
                Python Collections (Arrays)
There are four collection data types in the Python programming language:

1]List is a collection which is ordered and changeable. Allows duplicate members.
2]Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
3]Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
4]Dictionary is a collection which is ordered** and changeable. No duplicate members.

add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
'''


List1=['a',3,4,'Ajay']
tuple2=('a',3,4,'Ajay')
Sets3={'a',3,4,'Ajay'}
Dic={'Name':'Ajay','GF_Name':'Chaitrali P'}

print("List1",List1)
print("tuple2",tuple2)
print("Sets3",Sets3)
print("Dic",Dic)
