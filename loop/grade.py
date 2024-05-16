#Enter subject marks and calculate percentage and find its grade
marathi=int(input("Enter marathi sub mark:"))
hindi=int(input("Enter hindi sub mark:"))
english=int(input("Enter english sub mark:"))

total=marathi+hindi+english
per=total/3
print("\nTotal mark:",total," Percentage:",per)

if per>=90:
    print("Grade A")
elif per<90 and per>=80:
    print("Grade B")
elif per<80 and per>=60:
    print("Grade C")
elif per<60 and per>=40:
    print("Grade D")
else:
    print("Fail")