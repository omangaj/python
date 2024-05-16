from array import *
arr=array("i",[])
size=int(input("Enter size of array:"))
for i in range(0,size):
    arr.append(int(input("Enter element:")))

for i in arr:
    print(i,end=" ")


arr2=array("i",[])

arr2=arr.__copy__()

for i in arr2:
    print(i,end=" ")

