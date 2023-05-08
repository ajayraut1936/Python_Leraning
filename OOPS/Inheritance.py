'''
Inheritance :  Child class can use methods of Parent  class
'''

class   parent:                             #Parent Class
    def __init__(self,name,lname):
        self.name=name
        self.lname=lname

    def description(self):                      #parent_method
            print("this is just Parent Fuction")

class child(parent):                        #Child class
    def child1(self):                       #child method
        print("this is child")


obj_parent=parent("Ajay","Raut")            #parent object creation
print(obj_parent.description())                  #calling method with object


obj_child=child("Abh","raut")               #child object creation
print(obj_child.child1())                     #calling method with object\
print(obj_parent.description())               #calling method with object



