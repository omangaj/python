l=[]
n=int(input("enter length of list l:"))
for i in range(n):
    l.append(int(input("Enter value:")))

for i in l:
    print(i,end=" ")

index=int(input("\nEnter index to insert value:"))
value=int(input("Enter value to insert index:"))

l.insert(index,value)
for i in l:
    print(i,end=" ")