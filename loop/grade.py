marathi=int(input("Enter marathi sub mark:"))
hindi=int(input("Enter hindi sub mark:"))
english=int(input("Enter english sub mark:"))

total=marathi+hindi+english
print("Total mark:",total)
per=total/3
print("Percentage:",per)

if per>=90:
    print("Grade A")
elif per<90 and per>=80:
    print("Grade B")
elif per<80 and per>=70:
    print("Grade C")
elif per<70 and per>=60:
    print("Grade D")
else:
    print("Fail")