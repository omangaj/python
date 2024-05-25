from array import *
def large():
    arr=array("i",[])
    size=int(input("Enter size of arr:"))
    for i in range(0,size):
        arr.append(int(input("Enter element:")))

    mx=max(arr)
    return mx

a=large()
print("largest no in array:",a)