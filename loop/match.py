#Enter two number and choose any arithmetic operation
a=int(input("Enter value:"))
b=int(input("Enter value:"))
print("1.addition")
print("2.subtraction")
print("3.divide")
print("4.multiplication")
choice=int(input("Enter choice"))
match(choice):
    case 1:
        c=a+b
        print("addition of a and b=",c )
    case 2:
        c=a-b
        print("subtraction of a and b=", c)
    case 3:
        c=a/b
        print("divide of a and b=", c)
    case 4:
        c=a*b
        print("multiplication of a and b=",c)