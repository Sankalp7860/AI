import numpy as np
arr2 = np.random.rand(5,6)
flattened_array = arr2.flatten()
unique_values, counts = np.unique(flattened_array, return_counts=True)
frequency_dict = dict(zip(unique_values, counts))
print("Original 2D Array:")
print(arr2)
print("\nFrequency of Repeated Numbers:")
for num, freq in frequency_dict.items():
    print(f"Number {num}: {freq} times")
