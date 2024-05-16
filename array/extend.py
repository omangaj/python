from array import *
arr1=array("i",[])
size=int(input("Enter size of 1st array:"))
for i in range(0,size):
    arr1.append(int(input("Enter element:")))
for i in arr1:
    print(i,end=" ")

arr2=array("i",[])
size=int(input("\nEnter size of 2nd array:"))
for i in range(0,size):
    arr2.append(int(input("Enter element:")))
for i in arr2:
    print(i,end=" ")
print("\nextend array:")
arr1.extend(arr2)
for i in arr1:
    print(i,end=" ")