
string_sample= "This is My name Ajay raut and you are noting about. you are good"

# len() : returns the length of the string 
print("The Length of the string is :",len(string_sample))

# title() : it returns the every word of first letter in cap
print("The title word : ",string_sample.title())

# to check all string is first letter with uppar case
print("checking title kw :", string_sample.istitle())

# to convert string to lower case
print("converting string to lower : ",string_sample.lower())

# to check string is lower case or not 
print("checking string lower case or not :",string_sample.islower())

# to convert string to upper case
print("convert sring to upper case: ",string_sample.upper())

# to check that all string is upper or not 
print("to check upper or not :",string_sample.isupper())

# count("string",start=op,end=op) :used to get the count of the sub string into string 
print("total string occurence is ",string_sample.count("are",3,60)) 

# find(string,start,end) : used to get index of first occurence of substing into string 
print("total string find is ",string_sample.find("are",3,60)) 

# find(string,start,end) : used to get index of first occurence of substing into string 
print("total string index is ",string_sample.index("are",3,60)) 

# startwith()
print("start_with : ",string_sample.startswith("The"))
#endwith()
print("ends_with : ",string_sample.endswith("good"))
#isalnum()
print("alpha_numeric : ",string_sample.isalnum())

# isspace() : it check for the space
print("cehcking for the space ", string_sample.isspace())

#strip() : it removes the whitespace from both sides 
print("Removing white spaces: ", string_sample.strip())

#replace(string,re_string) : used to replace the substring from strin 
print("Ajay replaced with Chaitu",string_sample.replace("Ajay","Chaitu"))

#join(sencond_string):  it is used to join two string into one 
string2= "String2 Started here"
print("String joining :::",string_sample.join("string2"))


#partation() : make paratation based upon the string and convert into list
print("partation after effect: ",string_sample.partition("Ajay"))

#split() : splite the string based on the deleminator and convert into list 
print("splite function: ",string_sample.split(" "))

# check the type of the variable
print("String type is : ",type(string_sample))

print("\n\n\n")

# sum of all list no
lit_no=[2,5,4,66,5,4,55,2,2]
print("Sum of the list: ",sum(lit_no))

# sorted(iterable, key, reverse)
print("Print in accending order: ",sorted(lit_no))

string_split=string_sample.split()
print("Print in accending order: ",sorted(string_split,key=lambda x: len(x)))


#ZIP()
l1=(5,6,7,8,9)
l2=(1,2,3,4,5)
l3=(10,11,12,13,14)
zipped_data=zip(l1,l2,l3)
print(zipped_data)