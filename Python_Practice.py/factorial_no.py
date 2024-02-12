

def factorial(no):
    number=no
    fact=1
    for i in range(number,1,-1):
        fact=fact*i

    return   fact

input_no=int(input("enter no for calculate factorial: "))
print("\nFactorial of" ,input_no," is ",factorial(input_no))