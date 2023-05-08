'''
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.
'''

def myfunc():
    print("\n\nThis is my first fuction/method")

myfunc()


# Function with arguments
def newfuc(name,lname,gfname):
    print("My Name is :",name,lname,". My Gf is",gfname)

newfuc("Ajay",'Raut',"Chaitrali")


#default pram values

def newfuc1(name='ajay',lname='hoga',gfname='jana'):
    print("My Name is :",name,lname,". My Gf is",gfname)

newfuc1()
newfuc1(name='Raut')
newfuc1('Raut',"Chaitrali")
newfuc1("Ajay")