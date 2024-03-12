# Parameter	Description
# iterable	    Required. The sequence to sort, list, dictionary, tuple etc.
# key	        Optional. A Function to execute to decide the order. Default is None
# reverse	    Optional. A Boolean. False will sort ascending, True will sort descending. Default is False



sentance = "This is my fault and now i have to work on it so would you help me in this scenario please"

sentance = sentance.split()
sentance = sorted(sentance,key=len,reverse=True)
print(sentance)

print("\nThird largest no is : ",sentance[2])



# # sort the list of names based on lastname or first character of the lastname
names = ['steve jobs', 'bill gates', 'john doe', 'tim cook', 'laura turner', 'alex martin']

ajay= 'steve jobs'

# print("\n\n",ajay.split()[-1])

print("Sorted values based on the last first names: ",sorted(names,key=lambda x:x.split()[-1]))



############################  Call the class in accending order based on age 
print("\n\n\n\nCall the class in accending order based on age ")
class Employee:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def __repr__(self):
        return f"{self.fname} {self.lname} ({self.age} years)"

# Instances of Employee
e1 = Employee("steve", "jobs", 26)
e2 = Employee("bill", "gates", 27)
e3 = Employee("amy", "masters", 28)
e4 = Employee("john", "dow", 22)

# List of employees
employees = [e1, e2, e3, e4]

# Sort employees based on their age
sorted_employees = sorted(employees, key=lambda x: x.age)

# Print sorted employees
for employee in sorted_employees:
    print(employee)

