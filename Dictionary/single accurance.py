t = [7,5,5,1,6,7,8,7,6]
d = {}
for value in t:
    if not value in d:
        d[value] = 1
    else:
        d[value] +=1
print(d)
for k in d:
    if d[k] == 1:
        print(k)