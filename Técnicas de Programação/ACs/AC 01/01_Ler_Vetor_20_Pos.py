# Faça uma função que leia um vetor V com 20 posições. Substitua a seguir,
# todos os valores nulos e negativos do vetor V por 1. Em seguida retorne
# o vetor alterado. Construa também um programa que teste a função criada.
# Faça upload de arquivos com a solução do problema solicitado.

# --------------- Function ---------------
def read_vector(vector):
       
    for index in range(20):
        if vector[index-1] <= 0:
            vector[index-1] = 1
    return vector
# ----------------------------------------

# --------------- Variavel ---------------
global_vector = [1, 0, 5, 15, -5, -3, -25, 0, 55, 15, 26, 97, 85, 99, 100, -35, 17, -2, 88, -3]
answer = read_vector(global_vector)
# ----------------------------------------

# --------------- Programa ---------------
print(answer)
# ----------------------------------------
