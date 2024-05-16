#calculate call bill
call=int(input("Enter calls:"))
if call<=100:
    print("bill amount=200")
elif call>100 and call<=150:
    bill=200+(call-100)*0.60
    print("bill amount=",bill)
elif call>150 and call<=200:
    bill=200+(call-100)*0.50
    print("bill amount=",bill)
else:
    bill=200+(call-100)*0.40
    print("bill amount=",bill)
