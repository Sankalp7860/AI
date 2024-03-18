import numpy as np
import time
P = np.random.rand(106, 104)
Q = np.random.rand(104, 106)

start_time = time.time()
result_loop = np.zeros((P.shape[0], Q.shape[1]))

for i in range(P.shape[0]):
    for j in range(Q.shape[1]):
        for k in range(Q.shape[0]):
            result_loop[i, j] += P[i, k] * Q[k, j]
t1 = time.time() - start_time
start_time = time.time()
result_vectorized = np.dot(P, Q)
t2 = time.time() - start_time
speedup =t1/t2

print("Matrix P:")
print(P)
print("\nMatrix Q:")
print(Q)

print("\nResult of Matrix Multiplication using Loops:")
print(result_loop)
print("\nResult of Vectorized Matrix Multiplication:")
print(result_vectorized)
print(f"\nTime taken for Matrix Multiplication using Loops: {t1:.6f} seconds")
print(f"Time taken for Vectorized Matrix Multiplication: {t2:.6f} seconds")
print(f"Speedup: {speedup:.2f}")
