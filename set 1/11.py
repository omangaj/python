p=int(input("Enter principle amount="))
t=int(input("Enter time="))
r=int(input("Enter rate="))

CI=p*(1+r/100)**t-p
print("total interest is=",CI)