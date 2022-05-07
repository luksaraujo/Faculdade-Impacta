# Elaborar uma função recursiva que calcule a soma dos números de 1 a N
# 1 + 2 + 3 + 4 + ... + N

def soma(n):
    if n <= 0:
        return 0
    else:
        return n + soma(n - 1)

print(soma(5))