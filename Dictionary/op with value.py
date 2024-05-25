l1 = ["ten", "five", "seven"]
l2 = [10, 5, 7]
result = dict(zip(l1,l2))               #list to dict
print(result)
#sum = 0
multi = 1
for i in result.values():
    #if i%2 == 0:                        #if value is even then adding it
    #    sum +=i
    if i%2 != 0:                         #if value is odd then multiply all odd values
        multi *= i
print(sum)
print(multi)