
#Comment

#1-         Single line comment
"""
dssd        -Multi line Comment
assd
"""


#Variable in Python
#   Variable - Variables are containers for storing data values.

a="Ajay"          #Double quite variable
b='Raut'          #Single quite varibale both we can use
c=23.5            #Flote value
d=23              #decimal value
e=True            #boolean value
f=False           #boolena value
print("\n\tVarious Variables in Python\n",a,b,c,d,e,f)


#IF want to define perticular data type then we use casting
# Basically casting is process of convert value from one data type into another

a=str("Ajay Loves Chaitrali")
b=int(23.50)
c=float(22)
d=bool(True)
print('\n\t Casting in Python\n',a,type(a),'\n',b,type(b),'\n',c,type(c),'\n',d,type(d))


#Assing multiple varibale onece
x,y,z='ajay','chaitrali','raut'
print("\nYour name is : ",y,x,z)
print(x+y+z)
print(x,y,z)

#Assign same values for multilple variables

x=y=z='chaitu'
print("\n Who was your Girlfriend : ",z)

#Variable type
'''
1] Global variable
2] Local variable

'''
x=" Global varibale"                                                        #Global Variables
def myfunc():
    x = "\n\nVariable Scope\nVaribale is : Local Variable"                  #Local Variables
    return x

myfunc()
print(myfunc())
print("Variable is : " + x)



#Declare global variable by global keyword
x=" Global varibale"                                                        #Global Variables
def myfunc():
    global x
    x = "\n\nVariable Scope\nVaribale is : Local Variable"                  #Local Variables
    return x

myfunc()
#print(myfunc())
print("Variable is : " + x)



## To get Random no pip package random
import random
print('\n\nRandom range from Random PIP LIb :',random.randrange(10,100))