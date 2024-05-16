#Enter string and covert into unique key dictonary
s=input("Enter string:").lower()
l=s.split(" ")
s1={}
for i in l:
    if i not in s1:
        s1[i]=0
        print(i,end=" ")
print("\n",s1)