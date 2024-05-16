mar=int(input("Enter marathi marks="))
eng=int(input("Enter english marks="))
hindi=int(input("Enter hindi marks="))

if mar>eng and mar>hindi:
    print("marathi")
if eng>mar and eng>hindi:
    print("english")
if hindi>mar and hindi>eng:
    print("hindi")

if mar>eng and mar<hindi or mar<eng and mar>hindi:
    print("marathi")
if eng>mar and eng<hindi or eng<mar and eng>hindi:
    print("english")
if hindi>mar and hindi<eng or  hindi<mar and hindi>eng:
    print("hindi")