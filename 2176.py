a = input()
b = []
for c in range(0, len(a)):
    b.append(int(a[c]))
soma = sum(b)
if soma % 2 == 0:
    a = a+'0'
    print(a)
else:
    a = a+'1'
    print(a)
