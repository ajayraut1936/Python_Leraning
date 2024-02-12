def palindrom_1():
    name=input("Enter string to validate: ")
    normal_string=name
    reverse_string=name[::-1]
    if  normal_string==reverse_string:
        print("Given string is palindrom")
    else:
        print("Given string is not palindrome")

def palindrom_2():
    name=input("Enter string to validate: ")
    normal_string=name
    size=len(name)
    variable=""
    for i in range(size,0,-1):
        # print(i)
        # print(name[i-1],end="")
        variable = variable + name[i-1]
        # print(variable)
    print(variable)
    if  normal_string==variable:
        print("It is and palindrome ",name)
    else:
        print("it is not pallindrome")
obj=palindrom_1()
obj=palindrom_2()

