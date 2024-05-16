from array import *
arr=array("i",[])
size=int(input("Enter size of array:"))
for i in range(0,size):
    arr.append(int(input("Enter element:")))

for i in arr:
    print(i,end=" ")
n=int(input("\nEnter value to want index:"))
ind=arr.index(n)
print(ind)