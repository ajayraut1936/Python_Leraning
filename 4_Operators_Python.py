##Operators

#Operators are used to perform operations on variables and values.

'''
Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Bitwise operators
Shift Operators

Arithmetic operators
+	Addition	        x + y
-	Subtraction	        x - y
*	Multiplication	    x * y
/	Division	        x / y
%	Modulus	            x % y
**	Exponentiation	    x ** y    #
//	Floor division	    x // y

'''
a=5
b=10
print("\n\t Arithmatic Operators ")
print('Addition         :',a+b)
print('Subtraction      :',a-b)
print('Multiplication   :',a*b)
print('Division         :',a/b)
print('Modulus          :',a%b)
print('Exponentiation   :',a**b)        ##same as 5*5*5*5*5*5*5*5*5*5
print('Floor division   :',a//b)        ##the floor division // rounds the result down to the nearest whole number


'''

Assignment operators
=	        x = 5	            x= 5
+=	        x += 3	            x = x + 3
-=	        x -= 3	            x = x - 3
*=	        x *= 3	            x = x * 3
/=	        x /= 3	            x = x / 3
%=	        x %= 3	            x = x % 3
//=	        x //= 3            	x = x // 3
**=	        x **= 3            	x = x ** 3
&=	        x &= 3	            x = x & 3
|=	        x |= 3	            x = x | 3
^=	        x ^= 3	            x = x ^ 3
>>=	        x >>= 3            	x = x >> 3
<<=	        x <<= 3            	x = x << 3

'''
print("\n \tAssignment Operators ")
x,y,z=2,10,15
print('Equal To :',x)                #1

x += 3
print("+= :",x)        #x=x+3
x=5
x-=3
print('-= :',x)         #x=x-3
x=5
x*=3
print('*= :',x)         #x=x*3
x=5
x/=3
print('/= :',x)         #x=x/3
x=5
x%=3
print('%= :',x)         #x=x%3





'''

Comparison operators
==	Equal	                            x == y
!=	Not equal	                        x != y
>	Greater than	                    x > y
<	Less than	                        x < y
>=	Greater than or equal to	        x >= y
<=	Less than or equal to	            x <= y

'''
print('\n\t Comparison operators')
x,y=5,10

if(x==y):                                       #equal [ == ]
    print('Both values are equal')
else:
    print('both values are not equal')

if(x!=y):                                       #Not equal	  [ != ]
    print('Both values are not equal')
else:
    print('both values are  equal')

if(x>y):                                       #Greater than [ > ]
    print('x is greter than y')
else:
    print('y is greter than x')

if(x<y):                                       #Less than	 [ < ]
    print('x is less than y')
else:
    print('y is less than x')

if(x<=y):                                       #Less than or equal to [ <= ]
    print('x is less than y')
else:
    print('y is less than x')
if(x>=y):                                       #Greater than or equal to [ >= ]
    print('x is greter than y')
else:
    print('y is greter than x')


'''
Logical operators
and 	        Returns True if both statements are true	                        x < 5 and  x < 10
or	            Returns True if one of the statements is true	                    x < 5 or x < 4
not	            Reverse the result, returns False if the result is true	not         (x < 5 and x < 10)


Identity operators
is 	            Returns True if both variables are the same object	x is y
is not	        Returns True if both variables are not the same object	x is not y


Membership operators
in 	            Returns True if a sequence with the specified value is present in the object	x in y
not in	        Returns True if a sequence with the specified value is not present in the object	x not in y

Bitwise operators
& 	AND	                    Sets each bit to 1 if both bits are 1	x & y
|	OR	                    Sets each bit to 1 if one of two bits is 1	x | y
^	XOR	                    Sets each bit to 1 if only one of two bits is 1	x ^ y
~	NOT	                    Inverts all the bits	~x
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2
>>	Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2
'''