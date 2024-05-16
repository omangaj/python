l=[]
n=int(input("Enter length of l:"))

for i in range(n):
    l.append(int(input("Enter element:")))
for i in l:
    print(i)
print("----------------")
k=1
for j in lst:
    for i in lst:
        if j==i:
            l.remove(l[j])
            k=k+1
            j=j+1

for i in l:
    print(i)