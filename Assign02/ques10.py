import numpy as np
print("\n\nQ10\n")
matrix = np.arange(1, 21).reshape(4, 5)
print("\n4x5 Matrix with Values Ranging from 1 to 20:")
print(matrix)


arr_zeros = np.zeros(10).astype(np.int32)
arr_ones = np.ones(10).astype(np.int32)
arr_fives = np.full(10, 5)
print("Array of 10 Zeros:")
print(arr_zeros)
print("\nArray of 10 Ones:")
print(arr_ones)


print("\nArray of 10 Fives:")
print(arr_fives)


arr_even = np.arange(10, 51, 2)
print("\nArray of Even Integers from 10 to 50:")
print(arr_even)

print("\nRandom Number between 0 and 1:")
print(np.random.rand())


np.savetxt("AI/matrix.txt", matrix)

load_matrix = np.loadtxt("matrix.txt")
print("\n Matrix from File:")
print(load_matrix.astype(np.int32))

