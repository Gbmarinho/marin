a, b = input().split()
a = int(a)
b = int(b)
mapa = []
cor = []
for ma in range(0, a):
    a = list(map(int, input().split()))
    mapa.append(a)
if (len(mapa) > 3 or len(mapa) == 3) and (len(mapa[0]) > 3 or len(mapa[0]) == 3):
    for co in range(1, len(mapa)-1):
        for ni in range(1, len(mapa[0])-1):
            if mapa[co][ni] == 42:
                if mapa[co-1][ni] == 7 and mapa[co-1][ni-1] == 7 and mapa[co-1][ni+1] == 7:
                    if mapa[co][ni-1] == 7 and mapa[co][ni+1] == 7:
                        if mapa[co+1][ni] == 7 and mapa[co+1][ni-1] == 7 and mapa[co+1][ni+1] == 7:
                            cor.append(co)
                            cor.append(ni)
                            break
else:
    cor.append(0)
    cor.append(0)
if len(cor) == 0:
    print('0 0')
else:
    print(f'{cor[0]+1} {cor[1]+1}')
