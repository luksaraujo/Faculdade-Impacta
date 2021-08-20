# Sejam dois conjuntos, A e B, com n e m elementos
# respectivamente. Não estão ordenados. Faça um
# programa em Python com:
# uma função (USANDO METODOS DE VARIAVEL ESTRUTURA
# - SETs) para:
# -  efetuar a intersecção entre dois conjuntos, ou
# seja, os elementos em comum entre os dois conjuntos.
# O conjunto C conterá a intersecção de A e B.
# Exemplo:
# A = { 7, 2, 5, 8, 4} e B= {4, 2,  5}, C = A ∩ B = {2, 5, 4}
# A = { 3, 9, 11} e B= {2, 6, 1}, C = A ∩  B = {}

def intersecao(x, y):
    C = x & y
    return C

A = {7, 2, 5, 8, 4}
B = {4, 2, 5}

C = intersecao(A, B)
print(C)
