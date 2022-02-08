n_1 = input()
n_2 = input()
n_3 = input()
if n_1 == 'vertebrado':
    if n_2 == 'ave':
        if n_3 == 'carnivoro':
            print('aguia')
        if n_3 == 'onivoro':
            print('pomba')
    if n_2 == 'mamifero':
        if n_3 == 'onivoro':
            print('homem')
        if n_3 == 'herbivoro':
            print('vaca')
if n_1 == 'invertebrado':
    if n_2 == 'inseto':
        if n_3 == 'hematofago':
            print('pulga')
        if n_3 == 'herbivoro':
            print('lagarta')
    if n_2 == 'anelideo':
        if n_3 == 'onivoro':
            print('minhoca')
        if n_3 == 'hematofago':
            print('sanguessuga')
