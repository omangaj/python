from array import *
arr=array("i",[])
size=int(input("Enter size of array:"))
for i in range(0,size):
    arr.append(int(input("Enter element:")))
c=int(input("Enter value:"))
cnt=arr.count(c)
print(cnt)