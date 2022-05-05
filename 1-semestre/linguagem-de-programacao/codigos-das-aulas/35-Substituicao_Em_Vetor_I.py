'''
Faça um programa que leia um vetor X[10]. Substitua a
seguir, todos os valores nulos e negativos do vetor X
por 1. Em seguida mostre o vetor X.

Entrada
A entrada contém 10 valores inteiros, podendo ser
positivos ou negativos.

Saída
Para cada posição do vetor, escreva "X[i] = x", onde i
é a posição do vetor e x é o valor armazenado naquela posição.
'''

x = [] # Declara o vetor
for contador in range(10):
    numero = int(input())
    if numero <= 0:
        x.insert(contador, 1)
    else:
        x.insert(contador, numero)

for contador2 in range(10):
    print(f'X[{contador2}] = {x[contador2]}')
