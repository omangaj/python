n=int(input("Enter number:"))

def sum(n):
    temp=n
    num=[]
    s=str(n)
    s1=s.strip()
    for i in s1:
        num.append(int(i))
    sum=0
    for i in num:
        sum +=i
    print("sum=",sum)

sum(n)