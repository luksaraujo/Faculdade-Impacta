def matriz_oposta(matriz):
    matriz_oposta = []
    for linha in matriz:
        linha_oposta = []
        for item in linha:
            linha_oposta.append(item * -1)
        matriz_oposta.append(linha_oposta)
    return matriz_oposta
