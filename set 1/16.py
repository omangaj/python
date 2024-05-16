l=[]
n=int(input("Enter length of l:"))
for i in range(n):
    l.append(int(input("Enter element:")))

for i in l:
    print(i,end=" ")
print("\nDivisible by 5:")
for i in l:
    if i%5==0:
        print(i,end=" ")
