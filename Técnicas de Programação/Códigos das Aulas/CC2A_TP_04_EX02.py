# Criar uma função em Python que recebe uma string e uma
# letra e retorna uma lista com as posições onde a letra
# é encontrada na string.
# Não usar a função count, index.

def posicao_letra(frase, letra):
    tamanho_frase = len(frase)
    posicoes = []
    frase = frase.lower()
    letra = letra.lower()
    for i in range(tamanho_frase):
        if frase[i] == letra:
            posicoes.append(i)
    return posicoes