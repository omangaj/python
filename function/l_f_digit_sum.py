n=int(input("Enter number:"))
def l_f_digit(n):
    s=str(n)
    l=s.strip()
    size=len(l)
    fd=l[0]
    ld=l[size-1]
    print("first digit=", l[0]," last digit=", l[size - 1])
    sum=int(fd)+int(ld)
    print("sum of first and last digit:",sum)

l_f_digit(n)