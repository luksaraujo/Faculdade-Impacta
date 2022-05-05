'''
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre
a soma dos números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a
soma dos valores ímpares que estão entre os valores
fornecidos na entrada que deverá caber em um inteiro.
'''

valor_1 = int(input())
valor_2 = int(input())
maior = valor_1 if valor_1 > valor_2 else valor_2
menor = valor_2 if valor_2 < valor_1 else valor_1
menor += 1
soma = 0
while (menor < maior):
    if (menor % 2 != 0):
        soma += menor
    menor += 1
print(soma)
