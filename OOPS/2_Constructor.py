class   game:
    def __init__(self,name , lastname):
        self.name=name
        self.lastname=lastname

    def printdata(self):
        print("My name is : "+self.name,self.lastname)

obj=game("Ajay","Raut")
print(obj.name,obj.lastname)
obj.printdata()



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
