#print number in reverse order
n=int(input("Enter number:"))
while n!=0:
    print(n,end=" ")
    n -=1
print("\n")
n = int(input("Enter number:"))
for i in range(n,0,-1):
    print(i,end=" ")