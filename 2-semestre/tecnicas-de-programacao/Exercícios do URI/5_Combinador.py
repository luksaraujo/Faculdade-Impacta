# Implemente um programa denominado combinador, que recebe duas strings e deve combiná-las, alternando as letras de cada string,
# começando com a primeira letra da primeira string, seguido pela primeira letra da segunda string, em seguida pela segunda letra
# da primeira string, e assim sucessivamente. As letras restantes da cadeia mais longa devem ser adicionadas ao fim da string
# resultante e retornada.

# Entrada
# A entrada contém vários casos de teste. A primeira linha contém um inteiro N que indica a quantidade de casos de teste que vem a
# seguir. Cada caso de teste é composto por uma linha que contém duas cadeias de caracteres, cada cadeia de caracteres contém entre
# 1 e 50 caracteres inclusive.

# Saída
# Combine as duas cadeias de caracteres da entrada como mostrado no exemplo abaixo e exiba a cadeia resultante.

cont = 0
qtd = int(input())

while cont < qtd:
    linha = input().split()
    palavra_1 = linha[0]
    palavra_2 = linha[1]
    final_palavra = ""
    cont2 = 0

    while cont2 < len(palavra_1) and cont2 < len(palavra_2):
        final_palavra += palavra_1[cont2] + palavra_2[cont2]
        cont2 += 1

    if cont2 < len(palavra_1):
        final_palavra+= palavra_1[cont2:]

    if cont2 < len(palavra_2):
        final_palavra += palavra_2[cont2:]
    
    print(final_palavra)
    cont += 1