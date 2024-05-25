def alpha():
    print("ABCD=65-90 and abcd=97-122")
    s=int((input("Enter starting ascii value:")))
    e=int((input("Enter ending ascii value:")))
    while s<=e:
        print(s,"=",chr(s))
        s+=1
alpha()