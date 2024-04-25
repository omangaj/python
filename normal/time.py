seconds = int(input("Enter the seconds = "))

hour = seconds // 3600
seocnds = seconds % 3600
minute = seconds // 60
seconds = seconds % 60

print("Hour =",hour)
print("Min = ", minute)
print("Sec = ", seconds)
