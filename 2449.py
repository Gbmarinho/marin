casos, altura_real = map(int, input().split())
lista_alturas = list(map(int, input().split()))
passos = 0
for i in range(len(lista_alturas) - 1):
    while lista_alturas[i] != altura_real:
        if(lista_alturas[i] > altura_real):
            lista_alturas[i] -= 1
            lista_alturas[i + 1] -= 1
        else:
            lista_alturas[i] += 1
            lista_alturas[i + 1] += 1
        passos += 1
if(lista_alturas[-1] != altura_real):
    passos += abs(lista_alturas[-1] - altura_real)
print(passos)
