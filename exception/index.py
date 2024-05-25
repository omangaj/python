l=[]
n=int(input("Enter size:"))
for i in range(n):
    l.append(int(input("Enter values:")))
try:
    for i in l:
        print(i,end=" ")
    ind=int(input("\nEnter index to pop value(out of range):"))
    index = l.pop(ind)
    for i in l:
        print(i,end=" ")
except IndexError as e:
    print(e)

for i in l:
    print(i,end=" ")
ind=int(input("\nEnter value to find index:"))
index = l.pop(ind)
for i in l:
    print(i,end=" ")