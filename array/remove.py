from array import *
arr=array("i",[])
size=int(input("Enter size of array:"))
for i in range(0,size):
    arr.append(int(input("Enter element:")))

for i in arr:
    print(i,end=" ")

r=int(input("\nEnter value to remove:"))
arr.remove(r)
for i in arr:
    print(i,end=" ")