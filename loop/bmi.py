h=float(input("Enter Height:"))
w=float(input("Enter weight:"))

bmi=w/(h*h)
print("bmi=",bmi)

if bmi<=18.5:
    print("Underweight")
elif bmi>18.5 and bmi<=24.9:
    print("Normal weight")
elif bmi>=25 and bmi<30:
    print("Overweight")
else:
    print("Obesity")