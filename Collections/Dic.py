#  Collection
'''
                Python Collections (Arrays)
There are four collection data types in the Python programming language:

1]List is a collection which is ordered and changeable. Allows duplicate members.
2]Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
3]Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
4]Dictionary is a collection which is ordered** and changeable. No duplicate members.

'''

List1=['a',3,4,'Ajay']
tuple2=('a',3,4,'Ajay')
Sets3={'a',3,4,'Ajay'}
Dic={'Name':'Ajay','GF_Name':'Chaitrali P'}

print("List1",List1)
print("tuple2",tuple2)
print("Sets3",Sets3)
print("Dic",Dic)

print("\n\n\t\" DICTIOANRY \"")
# Create Dic
thisDic={'Name':'Ajay','GF_Name':'Chaitrali P','Lname':'Raut'}

print("Get values by name :",thisDic['Name'])
#or
print("Get values by GF_Name :",thisDic.get("GF_Name"))

#lenght of Dic
print('Lenght of dic is :',len(thisDic))

#get list of all values
print(thisDic.values())

#Chnage the values
thisDic['Name']='Mahesh'
print(thisDic)

