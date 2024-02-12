
no=int(input("Enter no to check no is prime or not: "))

def prime_check(no):
    print("This is verifing prime or not",no)
    if no%2==0:
        print("This is Prime No")
    else:
        print("This is Not Prime No")

prime_check(no)