l=[]
n=int(input("Enter length of l:"))

for i in range(n):
    l.append(int(input("Enter element:")))
sum=0
try:
    for i in l:
        sum+=i
except Exception as e:
    print(e)
print("sum:",sum)