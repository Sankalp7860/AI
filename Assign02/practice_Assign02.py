import numpy as np
# Q1
print("Q1\n")
# file=open("/Users/sankalp/Desktop/Future_Work/AI/example.txt",'r')
file=open("AI/example.txt",'r')
for each in file:
    print(each)
    
# Q2
print("\n\nQ2\n")
file=open("AI/example.txt",'r')
print(file.read(9))

# Q3
print("\n\nQ3")
file2=open("AI/example.txt",'a')
file2.write("\nI am a Student.")
file2.close()

# Q4
print("\n\nQ4\n")
count=0
file3=open("AI/text.txt",'r')
for each in file3:
    if(each[0]!='T'):
        count=count+1
        print(each)
print(count)

# Q5
print("\n\nQ5\n")
file3=open("AI/text.txt",'r')
file4=open("AI/text2.txt",'w')
for each in file3:
    file4.write(each)

# Q6
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

# Q7
print("\n\nQ7\n")
a = np.array([[10,16,71,9],[71,91,31,51]])
print(a.ndim)
print(a.shape)
print(a.size)

# Q8
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


# Q9
print("\n\nQ9\n")
arr2 =((np.random.rand(8,7)*10)).astype(np.int32)
max_v = np.max(arr2, axis=0)
min_v = np.min(arr2, axis=0)
print(arr2)
print("Max values are:")
print("\n",max_v)
print("Min values are:")
print("\n",min_v)

# Q10
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

