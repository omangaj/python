l=[]
n=int(input("Enter length of l:"))

for i in range(n):
    l.append(int(input("Enter element:")))
sum=0
for i in l:
    sum+=i
print("sum:",sum)