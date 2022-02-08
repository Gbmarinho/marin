li = int(input())
op = str(input())
m = []
for i in range(12):
    l = []
    for j in range(12):
        l.append(float(input()))
    m.append(l)
s = sum(m[li])
if op == 'S': 
    print(f'{s:.1f}')
else: 
    print(f'{(s / 12):.1f}')
