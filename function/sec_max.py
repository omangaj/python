from array import *
def sec_mx():
    arr=array("i",[])
    size=int(input("Enter size of arr:"))
    for i in range(0,size):
        arr.append(int(input("Enter element:")))

    mx=max(arr)
    arr.remove(mx)
    mx2=max(arr)

    return mx2
a=sec_mx()
print("second largest no is:",a)
