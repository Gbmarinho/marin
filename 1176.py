fib = []
bi = []
a = 0
fib.append(a)
b = 1
fib.append(b)
h = a + b
fib.append(h)
for c in range(0, 60):
    a = b
    b = h
    h = a + b
    fib.append(h)
x = int(input())
for c in range(0, x):
    a = int(input())
    bi.append(a)
for c in range(0, len(bi)):
    print(f'Fib({bi[c]}) = {fib[bi[c]]}')
