# Sejam dois conjuntos, A e B, com n e m elementos
# respectivamente. Não estão ordenados. Faça um
# programa em Python com:
# uma função (USANDO LISTAS e SEM USAR METODOS DE
# SETs) para:
#
# - efetuar a intersecção entre dois conjuntos, ou
# seja, os elementos em comum entre os dois conjuntos.
# O conjunto C conterá a intersecção de A e B.
# Exemplo:
#
# A = { 7, 2, 5, 8, 4} e B= {4, 2,  5}, C = A ∩ B = {2, 5, 4}
# A = { 3, 9, 11} e B= {2, 6, 1}, C = A ∩  B = {}

def interseccao(list_1, list_2):
    list_3 = []
    for value_l1 in list_1:
        if (value_l1 in list_2) and (value_l1 not in list_3):
            list_3.append(value_l1)
    return list_3

A = [7, 2, 5, 8, 4]
B = [4, 2,  5]

print(interseccao(A, B))
