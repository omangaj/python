from array import *
def arr():
    arr1=array("i",[])
    size=int(input("Enter size of array:"))
    for i in range(0,size):
        arr1.append(int(input("Enter element:")))
    sum=0
    for i in arr1:
        sum+=i
    return sum


a=arr()
print("sum of array:",a)
