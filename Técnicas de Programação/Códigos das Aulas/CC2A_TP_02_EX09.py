# Escreva um programa em Python com uma função que, dada uma lista de números inteiros com n elementos, rearranje
# os elementos da lista de tal forma que todos os elementos menores ou iguais ao primeiro fiquem à sua esquerda e
# todos os outros, à sua direita.
# Exemplo:
# Na sequência {5, 6, 2, 7, 9, 1, 8, 3, 7} após ser rearranjada poderá ficar na forma:
#              {2, 1, 3, 5, 6, 7, 9, 8, 7}.

def rearranjar(lista):
    first_element = lista[0]
    lower_elements = []
    for element in lista:
        if element < first_element:
            lower_elements.append(element)
    lower_elements.append(first_element)
    for element in lista:
        if element > first_element:
            lower_elements.append(element)
    return lower_elements

lista_teste = [5, 6, 2, 7, 9, 1, 8, 3, 7]
print(rearranjar(lista_teste))