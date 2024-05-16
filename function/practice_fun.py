def cal():
    n1=int(input("Enter number 1:"))
    n2=int(input("Enter number 2:"))
    add=n1+n2
    sub=n1-n2
    mul=n1*n2
    return add,sub,mul


def check(x,l):
        if x in l:
            print("student present")
        else:
            print("student absent")

def mx(l):
    m=max(l)
    return m

def oddeven():
    n=int(input("Enter number:"))
    if n%2==0:
        print("This number is even")
    else:
        print("This number is odd")

def alpha(s):
    l=s.strip()
    vcount=0
    ccount=0
    for i in l:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
            vcount+=1
        else:
            ccount+=1
    print("vowels=", vcount)
    print("consonant=", ccount)


def fact(n):
    f=1
    for i in range(n,1,-1):
        f=f*i
    return(f)

def low_to_up():
    s=input("Enter string:")
    u=s.upper()
    return u

def rad():
    r=float(input("Enter radius:"))
    pi=3.14
    area=pi*r*r
    return area