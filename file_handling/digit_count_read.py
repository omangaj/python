def digit_count():
    fp=open(r"D:\class pune\python\sample.txt","r")
    content=fp.read()
    count=0
    for char in content:
        if char.isdigit():
            count=count+1
    print("The count is=",count)
    fp.close()

digit_count()