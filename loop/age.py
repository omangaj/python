#Enter age and find its category
age=int(input("Enter age:"))
if age<=12:
    print("Child")
elif age>=13 and age<=19:
    print("Teenager")
elif age>=20 and age<=59:
    print("Adult")
else:
    print("Senior Citizen")