def odd_sum():
    s = int(input("Enter starting value:"))
    e = int(input("Enter ending value:"))
    sum=0
    while s<=e:
        if s%2==1:
            sum+=s
        s+=1
    print("Sum of all natural odd no:",sum)

odd_sum()