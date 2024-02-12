#Python program to interchange first and last elements in a list

'''Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]'''

#Accpet list by User
lst=[]

no=int(input("Enter how many no wants to add in list: "))

for i in range(0,no):
    print(i)
    no=int(input("Enter list items : "))
    lst.append(no)
print(lst)

size=len(lst)
print("Size of list ",size)

#Method 1
#Swapping 

temp= lst[-1]
fst=lst[0]
lst[0]=temp
lst[-1]=fst



#Method 2
lst[0], lst[-1] =  lst[-1],lst[0]


# Method 3
lst=[2,4,3,5,6,7,4,5]
lst=lst[-1:] + lst[1:7] + lst[:1]

# print(lst[-1])
# print(lst[1])
# print(lst[1:7])
print(lst)


print("After swapping " , lst)
