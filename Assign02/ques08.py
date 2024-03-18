import numpy as np
print("\n\nQ8\n")
arr3 = (np.random.rand(3, 3)*10).astype(np.int32)  
arr4 = (np.random.rand(3, 3)*10).astype(np.int32)  

arr_con = np.concatenate((arr3, arr4))
print("Concatenated Array:")
print(arr_con)

arr5 = np.sort(arr3, axis=None)
arr6 = np.sort(arr4, axis=None)
print("\nSorted Array 1:")
print(arr5)
print("\nSorted Array 2:")
print(arr6)

arr_sum = arr3 + arr4
print("\nSum of Arrays:")
print(arr_sum)

arr_diff = arr3 - arr4
print("\nDifference of Arrays:")
print(arr_diff)

arr_mul = arr3 * arr4
print("\nProduct of Arrays:")
print(arr_mul)

arr_div=arr3/arr4
print("\nDivison of Arrays:")
print(arr_div)

