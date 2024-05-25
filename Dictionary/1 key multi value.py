even = []
odd = []

for i in range(6):
    n = int(input("Enter any number = "))

    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

d = {}
d['EVEN'] = even
d['ODD'] = odd

print(d)