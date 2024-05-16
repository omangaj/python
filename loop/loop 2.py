#print n numbers and separate into even and odd
num=int(input("Enter number:"))
for i in range(0,num):
    print(i,end=" ")
print("\neven number:")
for i in range(0,num,2):
    print(i,end=" ")
print("\nodd number")
for i in range(1,num,2):
    print(i,end=" ")


'''n=int(input("Enter number"))
for i in range(1,n):
    if i%2==0:
        print(i,end=" ")

for i in range(1,n):
    if i%2==1:
        print(i,end=" ")'''