#Enter number and find its factors
n=int(input("Enter number:"))
sum=0
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")