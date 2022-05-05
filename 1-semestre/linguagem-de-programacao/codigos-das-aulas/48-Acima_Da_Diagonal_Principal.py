matriz = []
operacao = input()
for i in range(12):
    matriz.append([])
    for j in range(12):
        valor = float(input())
        matriz[i].append(valor)

soma = 0
coluna = 1
cont = 0

for i in range(0, 11):
    for j in range(coluna, 12):
        soma += matriz[i][j]
        cont += 1
    coluna += 1

media = soma / cont

if operacao == 'M':
    print('{:.1f}'.format(media))
else:
    print('{:.1f}'.format(soma))
