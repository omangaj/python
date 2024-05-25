dict1 = {"twentyone":21,"nine":9, "seven":7, "fourtynine":49}
sum = 0
for i in dict1.values():
    if i%7==0:
        sum +=i
print(sum)