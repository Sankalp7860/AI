import numpy as np


A = np.random.rand(3, 3)
b = np.random.rand(3)
x = np.linalg.solve(A, b)
print("Coefficient Matrix A:")
print(A)
print("\nVector b:")
print(b)
print("\nSolution Vector x:")
print(x)
