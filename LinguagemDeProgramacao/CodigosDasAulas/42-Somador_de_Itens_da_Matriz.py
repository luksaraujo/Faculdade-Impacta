def somador_de_matrizes(matriz):
    soma = 0
    for linha in matriz:
        for posicao in linha:
            soma += posicao
    print(soma)

somador_de_matrizes([[1, 2, 3], [3, 2, 1]])
