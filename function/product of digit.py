n=int(input("Enter number:"))

def product(n):
    temp=n
    num=[]
    s=str(n)
    s1=s.strip()
    for i in s1:
        num.append(int(i))
    pro=1
    for i in num:
        pro *=i
    print("product=",pro)

product(n)