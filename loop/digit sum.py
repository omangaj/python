#Enter nuber and find sum of its digits
n=int(input("Enter number:"))
sum=0
while n!=0:
    rem=n%10
    n=n//10
    sum+=rem
print("sum=",sum)