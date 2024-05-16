lst=[]
n=int(input("Enter length of lst:"))
for i in range(n):
    lst.append(int(input("Enter elements:")))

l=len(lst)
if l!=0:
    print("lst not empty")
else:
    print("lst empty")