from array import *
arr=array("i",[])
size=int(input("Enter size of array:"))
for i in range(0,size):
    arr.append(int(input("Enter element:")))

for i in arr:
    print(i,end=" ")

arr.pop()
print("\nAfter pop")
for i in arr:
    print(i,end=" ")

index=int(input("\nEnter index:"))
arr.pop(index)
print("After pop with index")
for i in arr:
    print(i,end=" ")