str1 = input("Enter string to print :")
words = str1.strip()
d = {}
for w in words:
    if not w in d:
        d[w]= 0
        print(w,end=" ")
print("\n",d)