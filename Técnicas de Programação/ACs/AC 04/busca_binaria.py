def busca_binaria(v, x):
    print(v)
    bubble_sort(v)
    print(v)
    ini = 0
    fim = len(v) - 1
    while ini <= fim:
        meio = (ini + fim) // 2
        if v[meio] == x: # Encontrou o valor buscado
            return v[meio] 
        elif x > v[meio]: # Busca na segunda metade
            print(v[meio])
            ini = meio + 1
        else: # Busca na primeira metade
            print(v[meio])
            fim = meio - 1
    return -1 # Não encontrou

def bubble_sort(list_to_sort):
    elements = len(list_to_sort) - 1
    is_list_sorted = False
    while not is_list_sorted:
        is_list_sorted = True
        for i in range(elements):
            if list_to_sort[i] > list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
                is_list_sorted = False
    return list_to_sort

# lista = [1,5,18,15,25,50,100]
# lista = [3,10,45,75,78,95,105,110]
# print(busca_binaria(lista, 46))
