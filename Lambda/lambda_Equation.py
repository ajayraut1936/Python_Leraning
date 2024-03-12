# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.



x = lambda a: a+5

print("Lambda : ",x(5))


x =  lambda a,b: a+b

print("Lambda : ",x(4,60))



# Sort no by using lambda function 

list1= [5,4,33,44,66,33,1,2,0,4,34,5645,4,234,23,4,23]

print(list1)

# sorted_list= sorted(list1,key=lambda x:-x)


sorted_list= sorted(list1,reverse=True)

print(sorted_list[2])



# sort letters in sentance 

sentance = "This is my fault and now i have to work on it so would you help me in this scenario please"

sentace_sort = sentance.split()
sentace_sort = sorted(sentace_sort,key=len,reverse=True)

print(sentace_sort)


# sorted_sentance = sorted(sentance, key=lambda x : x.split()[-1])

# print("Sorted sentance list: ",sorted_sentance)


# print("Sorted list is: ",sorted_list)