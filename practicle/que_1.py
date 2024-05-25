from array import *
class arr:
    def __init__(self,arr1):
        self.arr1=arr1

    def displaydata(self):
        for i in arr1:
            print(i,end=" ")
    def difference(self):
        d = int(input("\nEnter diff of two values:"))
        for i in arr1:
            for j in arr1:
                if i - j == d:
                    print(i, "and", j)


n=int(input("Enter array size:"))
arr1=array("i",[])
for i in range(0,n):
    arr1.append(int(input("Enter element:")))

a=arr(arr1)
a.displaydata()
a.difference()
