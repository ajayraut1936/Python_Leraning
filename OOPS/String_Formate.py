#23/03/22
#String Formating in Python

name='Ajay'
lname ='raut'
age=24
address='ap.ladegoan tal-khatav dist- satara'

#   String Formate by Multiple Values
formated_string='My name is {} {} and i am {} old and My Adress is : {}'

#   String Formate By index
formated_string1='My name is {0} {1} and i am {2} old and My Adress is : {3}'

#   String Formate By name
formated_string2='My name is {name1} {lname1} and i am {age1} old and My Adress is : {addr}'


print(formated_string.format(name,lname,age,address))
print(formated_string1.format(name,lname,age,address))
print(formated_string2.format(name1=name,lname1=lname,age1=age,addr=address))

