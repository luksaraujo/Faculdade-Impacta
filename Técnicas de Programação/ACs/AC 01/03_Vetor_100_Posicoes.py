# Faça um programa que leia um vetor com 100 posições. No final,
# mostre todas as posições do vetor que armazenam um valor maior ou
# igual a 10, o valor armazenado em cada uma das posições e a média
# desses valores. Faça upload de arquivos com a solução do problema
# solicitado.

import random

# --------------- Function ---------------
def read_vector_100_positions(vector):
    vector_size = len(vector)
    positions = f"Posições com valores maiores ou iguais a 10: "
    values = f"Valores nas respectivas posições: "
    divider = 0
    dividend = 0
    for index in range(vector_size):
        if vector[index] >= 10:
            positions += f"{index}, "
            values += f"{vector[index]}, "
            divider += vector[index]
            dividend += 1
    average = divider / dividend
    positions = positions[:-2]
    values = values[:-2]
    print("\n", positions, "\n")
    print(values, "\n")
    print(f"A média dos valores maiores ou iguais a 10 é de {average:.1f}")
    return None
# ----------------------------------------

# --------------- Variavel ---------------
global_vector = []
# ----------------------------------------

# --------------- Programa ---------------
try:
    for _ in range(100):
        global_vector.append(random.choice(range(100)))
    read_vector_100_positions(global_vector)
except ZeroDivisionError:
    print("Não é possível dividir um número por zero! Talvez nenhum número no seu vetor seja maior ou igual a 10.")
except:
    print("Um erro desconhecido aconteceu")
# ----------------------------------------