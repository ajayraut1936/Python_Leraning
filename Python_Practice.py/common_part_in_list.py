
ls1=[2,4,53,5,6,3,4,2,5,7]
ls2=[3,5,7,3,6,7,3,5,53,55,66,77]

com_ls=[]
for i in ls1:
    print(i)
    for j in ls2:
        print(j)
        if i==j:
            com_ls.append(i)
        
print("common list",com_ls)
