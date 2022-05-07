# Crie um função que receba como parâmetro uma matriz
# tridimensional de inteiros e um número N e retorne
# a soma de todos os valores pares que estão na matriz
# e que são maiores que N
# Crie também um programa que preencha a matriz com números
# aleatórios e chame a função criada

import numpy as np
import random

def blevers(MAT, N):
    soma_pares_maiores_que_N = 0
    nX = len(MAT)
    for x in range(nX):
        nY = len(MAT[x])
        for y in range(nY):
            nZ = len(MAT[x][y])
            for z in range(nZ):
                if MAT[x][y][z] > N and MAT[x][y][z] % 2 == 0:
                    soma_pares_maiores_que_N += MAT[x][y][z]
    return soma_pares_maiores_que_N

matriz = np.random.random_integers(low=0, high=9999, size=(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)))
print(blevers(matriz, 10))
