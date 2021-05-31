'''
Faça um algoritmo para ler um número indeterminado
de dados, contendo cada um, a idade de um indivíduo.
O último dado, que não entrará nos cálculos, contém
o valor de idade negativa. Calcular e imprimir a
idade média deste grupo de indivíduos.

Entrada
A entrada contém um número indeterminado de inteiros.
A entrada será encerrada quando um valor negativo for lido.

Saída
A saída contém um valor correspondente à média de idade dos indivíduos.

A média deve ser impressa com dois dígitos após o ponto decimal.
'''

idade_digitada = 0
total_idades = 0
qtde_idades = 0
while idade_digitada >= 0:
    idade_digitada = int(input())
    if idade_digitada >= 0:
        total_idades += idade_digitada
        qtde_idades += 1
media_idades = total_idades / qtde_idades
print(f'{media_idades:.2f}')
