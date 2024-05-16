from array import *
arr=array("i",[])
size=int(input("Enter size of array:"))
for i in range(0,size):
    arr.append(int(input("Enter element:")))

for i in arr:
    print(i,end=" ")
index=int(input("\nEnter index to insert value:"))
val=int(input("Enter value to insert index:"))
arr.insert(index,val)
for i in arr:
    print(i,end=" ")