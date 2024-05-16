s1=input("Enter string:")
n1=int(input("Please enter starting index to remove character:"))
n2=int(input("Please enter endind index to remove character:"))
s=""
for i in range(0,n1):
    s=s+s1[i]
for i in range(n2,len(s1)):
    s=s+s1[i]

print(s)