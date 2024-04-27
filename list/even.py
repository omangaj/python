lst=[]
n=int(input("how many element in list:"))
for i in range(n):
    lst.append(int(input("Enter element:")))

for i in lst:
    if i%2==0:
        print(i,end=" ")