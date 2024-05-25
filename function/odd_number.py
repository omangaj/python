def odd():
    s = int(input("Enter starting value:"))
    e = int(input("Enter ending value:"))
    print("Odd numbers")
    while s<=e:
        if s%2==1:
            print(s,end=" ")
        s+=1

odd()