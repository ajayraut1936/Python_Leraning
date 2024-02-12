num=[1,2,4,3,5,6,54,5,6,4,3,5,3,1,3,55,4,3,5]

size=len(num)

for i in range(0,size):
    print(i)
    count=0
    for j in num:
        if i==j:
            count+=1
    print("Count for ",i," is: ",count)