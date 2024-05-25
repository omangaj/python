import builtins
class absolute:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def data(self):
        print("a:",abs(a))
        print("b:",abs(b))
        print("c:",abs(c))

a=int(input("Enter + or - value a:"))
b=int(input("Enter + or - value b:"))
c=int(input("Enter + or - value c:"))

x=absolute(a,b,c)
x.data()