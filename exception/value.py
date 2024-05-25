l=[]
n=int(input("Enter size:"))
for i in range(n):
    l.append(int(input("Enter values:")))
print("remove value")
try:
    val=int(input("Enter value not present in list l:"))
    l.remove(val)
    for i in l:
        print(i,end=" ")
except ValueError as e:
    print(e)

val = int(input("Enter value present in list l:"))
l.remove(val)
for i in l:
    print(i, end=" ")

