from array import *
def avg():
    arr=array("i",[])
    size=int(input("Enter size of arr:"))
    for i in range(0,size):
        arr.append(int(input("Enter element:")))
    sum=0
    for i in arr:
        sum+=i
        average=sum/size

    return average

a=avg()
print("avarage of array:",a)