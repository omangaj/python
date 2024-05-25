fp=open(r"D:\class pune\python\number.txt","r")
sum=0
for line in fp:
    number=int(line.strip())
    sum=sum+number
    print(number)
fp.close()

print("sum=",sum)