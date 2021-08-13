'''
CC2A TP 01 EX06 - Criar uma função em Python
que recebe uma string e uma letra e retorna a
quantidade de ocorrências da letra na string
Não usar a função count
'''

#==================== FUNÇÕES ====================
def qtde_ocorrencias(string, letra):                # Inicializa a função
    qtde_de_ocorrencias = 0                         # Cria a variável que armazenará quantas vezes a letra aparece na string
    for i in string:                                # Atribui cada letra da string na variável i, uma por repetição
        i = i.upper()                               # Transforma a letra no i em uma letra maiúscula
        letra = letra.upper()                       # Transforma a letra em uma letra maiúscula
        if i == letra:                              # Se o conteúdo de i for igual ao conteúdo de letra
            qtde_de_ocorrencias += 1                # Incrementa 1 na quantidade de repetições
    return qtde_de_ocorrencias                      # Retorna a quantidade de ocorrências da letra na string
#=================================================

#=================== VARIÁVEIS ===================
string = input("Digite uma frase: ")                # Recebe uma frase
letra = input("Digite uma letra: ")                 # Recebe uma letra
#=================================================

#=================== PROGRAMA ====================
print(qtde_ocorrencias(string, letra))              # Exibe quantas vezes a letra aparece dentro da string
#=================================================
