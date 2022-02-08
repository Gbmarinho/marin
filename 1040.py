x = input().split()
a, b, c, d = x
n_1 =float(a)
n_2 =float(b)
n_3 =float(c)
n_4 =float(d)
media = ((n_1 * 2) + (n_2 * 3) + (n_3 * 4) + n_4) / 10
if media >= 7.0:
    print(f'Media: {media:.1f}')
    print('Aluno aprovado.')
if media < 5.0:
    print(f'Media: {media:.1f}')
    print('Aluno reprovado.')
if 5.0 <= media <= 6.9:
    print(f'Media: {media:.1f}')
    print('Aluno em exame.')
    n_5 = float(input())
    print(f'Nota do exame: {n_5:.1f}')
    m = (n_5 + media) / 2
    if m >= 5.0:
        print('Aluno aprovado.')
        print(f'Media final: {m:.1f}')
    else:
        print('Aluno reprovado.')
        print(f'Media final: {m:.1f}')
