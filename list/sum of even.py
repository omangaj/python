lst=[]
sum=0
n=int(input("how many element in lst:"))
for i in range(n):
    lst.append(int(input("Enter element:")))

for i in lst:
    if i%2==0:
        sum += i
        print(i,end=" ")

print("\nsum of even=",sum)