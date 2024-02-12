

string1=input("Enter any string")
# string1= "Ajay"
print(string1[1])
size=len(string1)
for i in range(size,0,-1):
    # print(i)
    print(string1[i-1],end=" ")


# or
print("\n\n")
print(string1[::-1])