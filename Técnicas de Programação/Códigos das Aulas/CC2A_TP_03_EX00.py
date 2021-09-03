def sum_matrix_elements(matrix):
    adder = 0
    for matrix_index in range(len(matrix)):
        for line_item in matrix[matrix_index]:
            adder += line_item
    return adder