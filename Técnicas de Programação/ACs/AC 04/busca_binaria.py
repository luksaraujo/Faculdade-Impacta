def busca_binaria(v, x):
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

# lista = [1,5,18,15,25,50,100]
# print(busca_binaria(lista, 18))
