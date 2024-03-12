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




print("\n\n\n")
Dic={'Name':'Ajay','GF_Name':'Chaitrali P','Age':25}

print(Dic)
# Print the lenght of the dic 
print(len(Dic))

# to check the type of dic 
print(type(Dic))

#to get something from dic by keys 
print(Dic.get("Name"))
print(Dic["Name"])

# to get all keys of the doc 
print(Dic.keys())

#to get all values of dic 
print(Dic.values())

# to get all items of dic 
print(Dic.items())

# Chnage item
Dic['Name']= "Chaitu"
print(Dic)

Dic.update({'Name':'Ajay'})
print(Dic)

Dic.update({'addr':'katraj'})
print(Dic)

Dic.pop("addr")
print(Dic)

del Dic["Name"]
print(Dic)

Dic.clear()
print(Dic)

# del Dic


Dic={'Name':'Ajay','GF_Name':'Chaitrali P','Age1':25,'Age2':24,'Age3':100}

for i in Dic:
    print(i)

def return_values(str):
    print(str)
    value=str.values()
    return value

# sorted_vales = sorted(Dic, key=lambda x:return_values(x))
my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 3}

# Sorting the dictionary based on values in ascending order
sorted_dict = sorted(my_dict.items(), key=lambda item: item[1])

print(sorted_dict)
