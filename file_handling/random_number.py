import random
fp=open(r"D:\class pune\python\number.txt","w")
n=int(input("How many number insert in file from(1 to 100):"))
for i in range(n):
    number=random.randint(1,100)
    fp.write(str(number)+"\n")
fp.close()

fp=open(r"D:\class pune\python\number.txt","r")
print(fp.read(2))
fp.close()