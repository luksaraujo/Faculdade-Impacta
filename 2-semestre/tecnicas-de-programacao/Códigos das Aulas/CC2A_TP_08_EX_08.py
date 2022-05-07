# Elaborar uma função recursiva que imprime os dígitos de um número
# Para 2365:
# 5
# 6
# 3
# 2

def imp(n):
    if n <= 0:
        return
    else:
        print(n % 10) # Isso exibe o último dígito do número inteiro
        imp(n // 10) # Isso remove o último dígito da direita