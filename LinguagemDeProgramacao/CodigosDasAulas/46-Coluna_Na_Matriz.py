matriz = []                                 # Inicializa a matriz que armazenará os dados
coluna_investigada = int(input())           # Valor inteiro correspondente à coluna a ser investigada
operacao = input()                          # Operação que será realizada com os valores da coluna (soma ou média)

for i in range(12):                         # Laço responsável por popular a matriz
    matriz.append([])                       # Insere uma linha por vez na matriz, da posição 0 à 11
    for j in range(12):                     # Adiciona um valor em cada posição da linha, de 0 a 12
        x = float(input())                  # Lê os valores que o usuário informará
        matriz[i].append(x)                 # Adiciona cada elemento ao final da última linha da matriz

soma = 0                                    # Armazena o valor da soma dos valores inseridos

for i in range(12):                         # Laço responsável por somar os valores da coluna
    soma += matriz[i][coluna_investigada]   # Soma os valores de cada linha na coluna indicada

media = soma / 12                           # Calcula a média

if operacao == "S":                         # Se o valor inserido for S
    print('{:.1f}'.format(s))               # Exibe a soma
else:                                       # Senão
    print('{:.1f}'.format(media))           # Exibe a média
