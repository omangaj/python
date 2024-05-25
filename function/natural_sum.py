def n_sum():
    s = int(input("Enter starting value:"))
    e = int(input("Enter ending value:"))
    sum=0
    while s<=e:
        sum+=s
        s+=1
    print("Sum of all natural no:",sum)

n_sum()