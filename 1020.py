x = int(input())
a = m = d = 0
a = x // 365
m = (x % 365) // 30
d = (x % 365) % 30
print(f'{a} ano(s)')
print(f'{m} mes(es)')
print(f'{d} dia(s)')
