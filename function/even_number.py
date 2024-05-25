def even():
    s = int(input("Enter starting value:"))
    e = int(input("Enter ending value:"))
    print("Even numbers")
    while s<=e:
        if s%2==0:
            print(s,end=" ")
        s+=1

even()