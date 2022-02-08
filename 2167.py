x = int(input())
cont = 0
menor = 0
maior = 0 
lista = [int(x) for x in input().split()]
maior = lista[0]
for c in range(0, len(lista)):
    cont = cont + 1
    if maior < lista[c]:
        maior = lista[c]
    if maior > lista[c]:
        print(cont)
        break
    if cont == x:
        print('0')
