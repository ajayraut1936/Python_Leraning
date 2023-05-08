'''
Python Classes/Objects
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

'''

class myclass:
    x=5;

print(myclass)
#Creating Object
object1=myclass()
#calling x value
print("The value of x form class is :",object1.x)

#Use of __init__()

# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:


class person:
    def __init__(self,name,lname,gfname):
        self.name=name
        self.lname=lname
        self.gfname=gfname

    def PrintData(self):
        print("\nYour name is :",self.name,"\nLname is :",self.lname,'\ngfname is :',self.gfname)

object12=person('Ajay','Raut','Chaitu')
object12.PrintData()


class Listname:
    def __init__(constructor,name):
        constructor.name=name

    def show(conc):
        print('\n\nName is :',conc.name)
p1=Listname('Sarveh')
p1.show()


'''
The __str__() Function
The __str__() function controls what should be returned when the class object is represented as a string.

If the __str__() function is not set, the string representation of the object is returned:

'''

class person:
    def __init__(self,name,lname,gfname):
        self.name=name
        self.lname=lname
        self.gfname=gfname

    def __str__(self):
        return f"{self.name},{self.lname}"
object12=person('Ajay','Raut','Chaitu')
print(object12)
