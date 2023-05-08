
#------------------->>>>#Python String

String = 'ajay loved one girl who reject z the ajay and now ajay is single '

print(String)
print(String[1:11])
print(String[-5:-3])

#Looping Through a String
for x in String:
    print(x)
    if(x=="z"):
        print("Lvl Done for z")
        break
print(len(String))

#Check String
print('si' in String)
if 'si' in String:
    print("si is Present in String ")

#check String present not
if 'reject'not in String:
    print("is Not ")
else:print("yes its working")

#   Multiline Stirng
multilineString="""S
sxss
s
s
d
sd
s
ds
"""
print(multilineString)
