a=int(input("Enter value a:"))
b=int(input("Enter value b:"))
try:
    c=a/b
    print("c=",c)
except ZeroDivisionError as e:
    print(e)

d=a+b
print("add=",d)