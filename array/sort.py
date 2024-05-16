from array import *
arr=array("i",[])
size=int(input("Enter size of array:"))
for i in range(0,size):
    arr.append(int(input("Enter element:")))

for i in arr:
    print(i,end=" ")

lst=arr.tolist()
lst.sort()
arr=array("i",lst)
print("\nsorted array:")
for i in arr:
    print(i,end=" ")