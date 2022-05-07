# Sejam dois conjuntos, A e B, com n e m elementos respectivamente. Não estão ordenados. Faça um programa em Python com:
# uma função (USANDO METODOS DE VARIAVEL ESTRUTURA - SETs) para:
# - efetuar a união de dois conjuntos. O conjunto C conterá todos os elementos de A e B, sem repetição.
# Exemplo:
# A = { 7, 2, 5, 8, 4} e B= {4, 2,5, 10}, C = A ∪ B = {7,2, 5,8, 4,10}
# A = { 3, 9, 11} e B= {2, 6, 1}, C = A ∪ B = {3,9,11,2,6,1}

def set_union(set_one, set_two):
    set_result = set_one.union(set_two)
    return set_result


A = {7, 2, 5, 8, 4}
B = {4, 2, 5, 10}
C = set_union(A, B)

print(C)
