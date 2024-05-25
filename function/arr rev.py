from array import *
def arr():
    arr1=array("i",[])
    s=int(input("Enter size of array:"))
    for i in range(0,s):
        arr1.append(int(input("Enter element:")))
    arr1.reverse()
    return arr1


a=arr()
for i in a:
    print(i,end=" ")
