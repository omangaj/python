n=int(input("Enter number:"))
def l_f_digit(n):
    s=str(n)
    l=s.strip()
    size=len(l)
    print("first digit=",int(l[0]))
    print("last digit=",int(l[size-1]))

l_f_digit(n)