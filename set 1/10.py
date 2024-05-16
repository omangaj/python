import math

a=int(input("Enter side 1="))
b=int(input("Enter side 2="))
c=int(input("Enter side 3="))

s=(a+b+c)/2
a=s*(s-a)*(s-b)*(s-c)
area= math.sqrt(a)
print("Area of rectangle:",area)