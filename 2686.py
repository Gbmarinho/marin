while True:
    try:
        M = float(input())
        if (M<=360):
            if (M < 90 or M == 360):
                print("Bom Dia!!")
            elif (M < 180):
                print("Boa Tarde!!")
            elif (M < 270):
                print("Boa Noite!!")
            elif (M < 360):
                print("De Madrugada!!")
        horas =(int(((M*240)/3600)%60)+6)
        if (horas>=24):
            horas = horas - 24
        minutos = (int((M*240)/60)%60)
        segundos =(int((M*240)%60))
        
        print(f'{horas:02}:{minutos:02}:0{segundos:00}')

    except EOFError:
        break
