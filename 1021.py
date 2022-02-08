n = float(input())
b = c = d = e = f = g = h = 0
m50 = m25 = m10 = m5 = m01 = 0
a = n // 100
b = (n % 100) // 50
c = ((n % 100) % 50) // 20
d = (((n % 100) % 50) % 20) // 10
e = ((((n % 100) % 50) % 20) % 10) // 5
f = (((((n % 100) % 50) % 20) % 10) % 5) // 2
g = ((((((n % 100) % 50) % 20) % 10) % 5) % 2) // 1
h = ((((((n % 100) % 50) % 20) % 10) % 5) % 2) % 1
h = h * 100
m50 = h // 50
m25 = (h % 50) // 25
m10 = ((h % 50) % 25) // 10
m5 = (((h % 50) % 25) % 10) // 5
m01 = ((((h % 50) % 25) % 10) % 5) // 1
print('NOTAS:')
print(f'{a:.0f} nota(s) de R$ 100.00')
print(f'{b:.0f} nota(s) de R$ 50.00')
print(f'{c:.0f} nota(s) de R$ 20.00')
print(f'{d:.0f} nota(s) de R$ 10.00')
print(f'{e:.0f} nota(s) de R$ 5.00')
print(f'{f:.0f} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{g:.0f} moeda(s) de R$ 1.00')
print(f'{m50:.0f} moeda(s) de R$ 0.50')
print(f'{m25:.0f} moeda(s) de R$ 0.25')
print(f'{m10:.0f} moeda(s) de R$ 0.10')
print(f'{m5:.0f} moeda(s) de R$ 0.05')
print(f'{m01:.0f} moeda(s) de R$ 0.01')
