import numpy as np
print("\n\nQ6\n")
def transpose_and_flatten(matrix):
    t_matrix = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        t_matrix.append(row)
        
    f_matrix = []
    for row in t_matrix:
        for element in row:
            f_matrix.append(element)

    return t_matrix, f_matrix
# ---------------------------------------------------------------------------------
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

t_result, f_result = transpose_and_flatten(matrix)

print("Transposed Matrix:")
for row in t_result:
    print(row)
    
print("Flattened Matrix:")
print(f_result)
