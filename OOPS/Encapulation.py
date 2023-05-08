class class_name:

    def __init__(self,name,lname):
        self._name=name                     #Protected Variable
        self.__lname=lname                    #Private Variable

    def info(self):
        return f" The My name is {self._name}. and last name is {self.__lname}"

obj1=class_name("Ajay","Raut")

print(obj1.info())