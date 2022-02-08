x = input().split()
inicio_h, inicio_m, final_h, final_m = x
inicio_h = int(inicio_h)
inicio_m = int(inicio_m)
final_h = int(final_h)
final_m = int(final_m)
if inicio_h < final_h:
    hora = final_h - inicio_h
    if inicio_m < final_m:
        minuto = final_m - inicio_m
    if inicio_m > final_m:
        hora = hora - 1
        minuto = (60 - inicio_m) + final_m
    if inicio_m == final_m:
        minuto = 0
if inicio_h > final_h:
    hora = (24 - inicio_h) + final_h
    if inicio_m < final_m:
        minuto = final_m - inicio_m
    if inicio_m > final_m:
        hora = hora - 1
        minuto = (60 - inicio_m) + final_m
    if inicio_m == final_m:
        minuto = 0
if inicio_h == final_h:
    if inicio_m < final_m:
        minuto = final_m - inicio_m
        hora = 0
    if inicio_m > final_m:
        minuto = (60 - inicio_m) + final_m
        hora = 23
    if inicio_m == final_m:
        hora = 24
        minuto = 0
print(f'O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)')
