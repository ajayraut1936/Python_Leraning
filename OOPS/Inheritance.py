# '''
# Inheritance :  Child class can use methods of Parent  class
# '''

# class   parent:                             #Parent Class
#     def __init__(self,name,lname):
#         self.name=name
#         self.lname=lname

#     def description(self):                      #parent_method
#             print("this is just Parent Fuction")

# class child(parent):                        #Child class
#     def child1(self):                       #child method
#         print("this is child")


# obj_parent=parent("Ajay","Raut")            #parent object creation
# print(obj_parent.description())                  #calling method with object


# obj_child=child("Abh","raut")               #child object creation
# print(obj_child.child1())                     #calling method with object\
# print(obj_parent.description())               #calling method with object




print("\n\n\n")

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def print_data(self):
        print("this is parent printing statement",self.name," : ",self.age)

class child02(student):
    def __init__(self,name,age,address):
        # self.name=name
        # self.age=age
        self.address=address
        super().__init__(name,age)                                                #with using the super() class
        # student.__init__(self,name,age)
    def print_data_child(self):
        print("This is Child class :",self.name,self.age,self.address)



obj = child02("Ajay",25,"Pune")

obj.print_data()

obj.print_data_child()





