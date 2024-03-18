import numpy as np

arr = np.random.rand(3, 3)
second_column = arr[:, 1]
last_row = arr[-1, :]
print("Original 2D NumPy Array:")
print(arr)
print("\nExtracted Second Column:")
print(second_column)
print("\nExtracted Last Row:")
print(last_row)
