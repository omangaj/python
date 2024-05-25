n=int(input("Enter number:"))
def l_f_digit(n):
    a=[]
    s=str(n)
    num=s.strip()
    size=len(num)
    for i in num:
        a.append(int(i))
    fd=a[0]
    ld=a[size-1]
    print("\n", fd, "   ", ld)
    for i in a:
        print(i,end="")
    a[0]=ld
    a[size-1]=fd
    fd=a[0]
    ld=a[size - 1]
    print("\n", fd, "   ", ld)
    for i in a:
        print(i,end="")
l_f_digit(n)
