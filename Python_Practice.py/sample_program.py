import math

str1 = "This is my string and i wanted to use it"
print(str1)
print(str1[::-1])

str1 = str1.split(" ")
print(str1)
str1 = sorted(str1,key=lambda x:len(x),reverse=True)
print(str1)

# a user has provided the string “D t C mpBl ckFrid yS le” and the character “a”, and the output will be “DataCampBlackFridaySale”.
string = "D t C mpBl ckFrid yS le"
replace_string= "a"

string_or = string.replace(" ","a")

print(string_or)


a=int(10)
val = math.sqrt(a)
print(val)
val = int(val)
print(val)
val = val*val
print(val)


# counting vovels in the list
vovels = ["a","e","i","o","u"]
string = "This is my Ajay nameu"
sub=0
for i in vovels:
    if i in string:
        sub=sub+1;
print("THE STRING VOVLES: ",sub)

print(string.count("a"))


# find middle of the string
string = "This is my Ajay nameu"
size = len(string)
size = int(size/2)
print("the size",size)
print(string[size+1])


# removing whitespaces
string = "C O D E"
string = string.strip()
string = string.replace(" ","")
print(string)


# occurence of words in string
string = "This is a white ocdoe"
for i in string:
    str = []
    j=0
    if j in string:
        str[i]+=1
    else:
        str[i]=1
print(str)