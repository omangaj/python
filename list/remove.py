lst = []
n = int(input("enter length of lst:"))
for i in range(n):
    lst.append(int(input("Enter value:")))

for i in lst:
    print(i, end=" ")

value = int(input("\nEnter value to remove from above lst:"))

lst.remove(value)
for i in lst:
    print(i, end=" ")