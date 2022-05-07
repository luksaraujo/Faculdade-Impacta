'''
CC2A TP EX01 - Criar um programa que preenche uma
lista com 5 elementos. Calcula a soma dos elementos
Imprime a soma dos elementos e todos os elementos da lista.
'''

#==================== FUNÇÕES ====================
#----------------- POPULAR LISTA -----------------
def popular_lista():
    for i in range(5):
        elemento = float(input(f"Digite o valor do {i+1}º elemento: "))
        lista.append(elemento)
#-------------------------------------------------
        
#---------------- SOMAR ELEMENTOS ----------------
def somar_elementos(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma
#-------------------------------------------------
#=================================================

#=================== VARIÁVEIS ===================
lista = []
#=================================================

#=================== PROGRAMA ====================
popular_lista()
soma_lista = somar_elementos(lista)
print(f'\nA soma dos elementos é igual a {soma_lista}')
print(lista)
#=================================================
