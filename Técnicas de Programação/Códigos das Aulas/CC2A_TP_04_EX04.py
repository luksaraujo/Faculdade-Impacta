# Criar um função que recebe por parâmetro uma matriz
# quadrada e retorna o maior valor encontrado nessa matriz
# Documentar a função como visto em aula

def higher_value(matrix):
    """
    Função higher_value
    Objetivo: Retorna o maior valor encontrado na matriz
    Entradas:
      matrix : uma matriz quadrada de números inteiros
    Saída:
      retorna o maior valor encontrado na matriz
    """
    higher_element = matrix[0][0]
    qtt_lines = len(matrix)
    for line in range(qtt_lines):
        for column in range(qtt_lines):
            if matrix[line][column] > higher_element:
                higher_element = matrix[line][column]
    return higher_element