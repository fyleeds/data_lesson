import numpy as np

#ndarray
# Creating a 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
# print(matrix)

# Accessing elements
# print(matrix[0, 1])  # Access the element in the first row, second column

# # Slicing
# print(matrix[:, 1])  # Get the second column
# print(matrix[1, :])  # Get the second row

# a = np.array([1, 2])
# b = np.array([3, 4])
# print(np.dot(a, b))

# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])
# print(np.matmul(A, B))

arr = np.zeros(10)
#convert to int
# print(arr.astype(int))

arr2 = np.zeros(10).astype(int).astype(str)
# print(arr2)
np.ones(10)
arr_full= np.full(fill_value=10, shape=(10, 10))
# print(arr_full)
arr_full= np.zeros((10, 10))

# print(arr_full)

arr_random = np.random.randint(0, 10, (10, 10)).astype(str) # 10x10 matrix with random integers between 0 and 10
# arr_random = np.random.seed(99,(10,10)) # 10x10 matrix with random integers between 0 and 10
# print(arr_random[-2:,-2:])

print(matrix.T)

moyenne = np.mean(matrix)   
print(moyenne)
ecart_type = np.std(matrix)
print(ecart_type)

