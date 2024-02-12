textstring=[1,3,4,54,65,340000,23,4,32,4,100,1000]
print(textstring)

init_values=0
for i in textstring:
    # print(i)
    
    if init_values<i:
        init_values=i
print("\nMost big value is : ",init_values)
