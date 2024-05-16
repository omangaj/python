sec= int(input("Enter the seconds = "))

hour=sec//3600
sec=sec%3600
min=sec//60
sec=sec%60

print("Hour=",hour)
print("Min=",min)
print("Sec=",sec)
