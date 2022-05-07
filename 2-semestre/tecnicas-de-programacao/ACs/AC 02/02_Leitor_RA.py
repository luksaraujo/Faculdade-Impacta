# Criar uma função que recebe uma matriz quadrada de ints e um núm int
# e retorna uma lista de tuplas com as posições (lin, col) onde o int é encontrado.

def positions(matrix, element):
    positions = []
    qtt_lines = len(matrix)
    qtt_columns = len(matrix[0])
    for line in range(qtt_lines):
        for column in range(qtt_columns):
            if matrix[line][column] == element:
                positions.append((line, column))
    return positions

# R.A. = 2100343
# RA com os 2 primeiros dígitos repetidos = 210034321

print("---- ENTRADAS ----")
quarto_digito = 0
matriz = [(2, 1, 0), (0, 3, 4), (3, 2, 1)]
print(f'Quarto dígito do R.A.: {quarto_digito}')
print(f'Matriz: {matriz}\n')
print('---- SAÍDA ----')
print(positions(matriz, quarto_digito))