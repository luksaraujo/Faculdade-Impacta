'''
Leia 100 valores inteiros. Apresente então o
maior valor lido e a posição dentre os 100
valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros,
positivos e distintos.

Saída
Apresente o maior valor lido e a posição de
entrada, conforme exemplo abaixo.
'''

maior_valor = 0
posicao = 0
for i in range(1, 101):
    valor = int(input())
    if valor > maior_valor:
        maior_valor = valor
        posicao = i
print(maior_valor)
print(posicao)
