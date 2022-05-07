# Sejam dois conjuntos, A e B, com n e m elementos respectivamente. Não estão ordenados. Faça um programa em Python com:
# uma função (USANDO LISTAS e SEM USAR METODOS DE SETs) para:
#
# - efetuar a união de dois conjuntos. O conjunto C conterá todos os elementos de A e B, sem repetição.
# Exemplo:
# A = { 7, 2, 5, 8, 4} e B= {4, 2,5, 10}, C = A ∪ B = {7,2, 5,8, 4,10}
# A = { 3, 9, 11} e B= {2, 6, 1}, C = A ∪ B = {3,9,11,2,6,1}

def list_union_no_repeat(list_a, list_b):
    list_c = []
    for element in list_a:
        list_c.append(element)
    for element in list_b:
        if element not in list_c:
            list_c.append(element)
    return list_c


a = [7, 2, 5, 8, 4]
b = [4, 2, 5, 10]
c = list_union_no_repeat(a, b)

print(c)
