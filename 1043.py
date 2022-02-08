x = input().split()
a, b, c = x
a = float(a)
b = float(b)
c = float(c)
if abs(b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    h = a + b + c
    print(f'Perimetro = {h:.1f}')
else:
    h = ((a + b) / 2) * c
    print(f'Area = {h:.1f}')
    
