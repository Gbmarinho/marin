cont = 0
lista = []
while True:
    contador = 0
    ca = input()
    if ca == '*':
        break
    else:
        c = ca.replace('/', ' ')
        compa = c.split()
    for g in range(0, len(compa)):
        for h in range(0, len(compa[g])):
            if compa[g][h] == 'W':
                cont = cont + 64
            if compa[g][h] == 'H':
                cont = cont + 32
            if compa[g][h] == 'Q':
                cont = cont + 16
            if compa[g][h] == 'E':
                cont = cont + 8
            if compa[g][h] == 'S':
                cont = cont + 4
            if compa[g][h] == 'T':
                cont = cont + 2
            if compa[g][h] == 'X':
                cont = cont + 1
        if cont == 64:
            contador = contador + 1
        cont = 0
    lista.append(contador)
for ki in lista:
    print(ki)
