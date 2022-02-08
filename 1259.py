par = []
impar = []
x = int(input())
for c in range(0, x):
    a = int(input())
    if a % 2 == 0:
        par.append(a)
    else:
        impar.append(a)
par.sort()
impar.sort()
impar.reverse() 
for b in par:
    print(b)
for y in impar:
    print(y)
