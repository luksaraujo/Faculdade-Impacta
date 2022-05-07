def pos_na_lista(lista, inteiro):
    existe_na_lista = inteiro in lista
    if existe_na_lista:
        posicao_na_lista = lista.index(inteiro)
        return posicao_na_lista
    else:
        return -1
