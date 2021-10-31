# Elaborar uma função recursiva que imprima os números de N a 1
# 3
# 2
# 1

def print_recursivo(n):
    print(n)
    if n > 1:
        print_recursivo(n - 1)
print_recursivo(3)