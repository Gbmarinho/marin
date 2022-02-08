hastes, altura_real_cerca = map(int, input().split())
lista = list(map(int, input().split()))
mov = 0
for i in range(len(lista) - 1):
    while lista[i] != altura_real_cerca:
        if(lista[i] > altura_real_cerca):
            lista[i] -= 1
            lista[i + 1] -= 1
        else:
            lista[i] += 1
            lista[i + 1] += 1
        mov += 1
if(lista[-1] != altura_real_cerca):
    mov += abs(lista[-1] - altura_real_cerca)
print(mov)
