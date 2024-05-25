lst1 = [7,3,8]
lst2 = ["python", "java", "sql"]
result = dict(zip(lst1,lst2))           #Combining two list to dictionary
print(result)
sum = 1
for i in result.keys():
    if i%2==0:         #for adding
        sum += i
    if i%2==0:          #for multiplication
        sum *= i
print(sum)
