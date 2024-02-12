str=[3,5,6,3,5,44,5,33,44,888,65,89,99,101,106,44,345]

init_values=0
for i in str:
    # print(i)
    
    if init_values<i:
        init_values=i
        str.remove('888')

print("\nMost big value is : ",init_values)

        
