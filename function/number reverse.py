n=int(input("Enter number:"))
def rev(n):
    try:
        temp=[]
        s=str(n)
        l=s.strip()
        for i in l:
            temp.append(int(i))
        temp.reverse()
        print(n)
        for i in temp:
            print(i,end="")
    except exception as e:
        print(e)

rev(n)