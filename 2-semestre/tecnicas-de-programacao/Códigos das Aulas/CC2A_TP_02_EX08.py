# A intercalação é o processo utilizado para construir uma lista ordenada, de tamanho n+m, a partir de duas listas já ordenadas
# de tamanhos n e m. Por exemplo, a partir das sequências abaixo:
# Exemplo:
# A = { 1, 3, 6, 7} e B= {2, 4, 5}, a nova lista C é feita a partir de A  e B:
# C = { 1, 2, 3, 5, 6, 7}
# Escreva um programa em Python com uma função que faça a intercalação entre duas listas.

def intercalacao(lista_1, lista_2):
    resposta = lista_1 + lista_2
    resposta[::2] = lista_1
    resposta[1::2] = lista_2
    return resposta

list1 = [1, 4, 5]
list2 = [3, 8, 9]

print(intercalacao(list1, list2))
