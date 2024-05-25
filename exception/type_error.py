a=int(input("Enter number:"))
b=int(input("Enter number:"))
try:
    c=str(a)+b
    print("c=",c)
except TypeError as e:
    print(e)


c=a+b
print("c=",c)