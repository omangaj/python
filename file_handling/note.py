fp=open(r"D:\class pune\python\Note.txt","w")
fp.write("@ The team achieved a milestone in 2023. They completed a multi-million-dollar project ahead of schedule. Stakeholders were impressed with a 98% success rate.")
fp.close()


fp=open(r"D:\class pune\python\Note.txt","r")
content=fp.read()
words=content.split()
for word in words:
    l=len(word)
    if l>=7:
        print(word)
fp.close()

print("\n-----------------")

fp=open(r"D:\class pune\python\Note.txt","r")
content=fp.read()
for word in content:
    if word<=chr(64) and word>=chr(91) or word<=chr(97) and word>=chr(123):
        print(word)
fp.close()
