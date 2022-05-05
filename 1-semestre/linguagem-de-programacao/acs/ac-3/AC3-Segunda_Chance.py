loops = int(input())
notas_originais=[]
notas_atividades=[]

for i in range(loops):
    notas_originais.append(float(input()))

for i in range(loops):
    notas_atividades.append(float(input()))

notas_finais = []
n_alteradas = 0

for i in range(loops):
    n_original = notas_originais[i]
    n_atividade = notas_atividades[i]
    n_final = n_original

    if(n_atividade == 10):
        n_final += 2

    if(n_final > 10):
        n_final = 10

    if(n_final != n_original):
        n_alteradas += 1

    notas_finais.append([n_original, n_final])
    
print(f'NOTAS ALTERADAS: {n_alteradas}')
for i, nota in enumerate(notas_finais):
    alt = '-'
    if(nota[0] != nota[1]):
        alt='*'

    print(f'{alt}({(i+1):03d}) original: {nota[0]:05.2f} | final: {nota[1]:05.2f}')
