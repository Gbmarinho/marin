x = int(input())
a, b, c = map(str, input().split())
a = int(a)
c = int(c)
if b == '*':
    y = a * c
    if y > x:
        print('OVERFLOW')
    else:
        print('OK')
if b == '+':
    y = a + c
    if y > x:
        print('OVERFLOW')
    else:
        print('OK')
