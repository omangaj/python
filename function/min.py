from array import *
def small():
    arr=array("i",[])
    s=int(input("Enter size of array:"))
    for i in range(0,s):
        arr.append(int(input("Enter element:")))

    mn=min(arr)
    return mn
a=small()
print("smallest value is:",a)