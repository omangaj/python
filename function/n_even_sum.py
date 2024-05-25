def even_sum():
    s = int(input("Enter starting value:"))
    e = int(input("Enter ending value:"))
    sum=0
    while s<=e:
        if s%2==0:
            sum+=s
        s+=1
    print("Sum of all natural even no:",sum)

even_sum()