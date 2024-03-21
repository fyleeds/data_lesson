import numpy as np

#ndarray
# Creating a 2D array (matrix)
matrix = np.array([[1, 2], [4, 5]])

# print(matrix==2)
# print(matrix>np.mean(matrix))
# print(np.mean(matrix))
# print(np.logical_and(matrix>np.mean(matrix), matrix<5))
# print(np.logical_or(matrix>np.mean(matrix), matrix<4))

filtre=[[True, False], [False, True]]
# print(matrix[filtre])

rnd_A = np.random.randint(0, 100, (10,10))
# print(rnd_A)

filtre = rnd_A > 50

# print(rnd_A[filtre])

# print(rnd_A[np.logical_and(rnd_A>50, rnd_A<70)])

indices = np.where(np.logical_and(rnd_A>50, rnd_A<55))

# print(indices)

# print(rnd_A[indices[0][2]], [indices[1][2]])

data= np.array([[1,1,1], [1,1,1], [1,0,1]])
print(np.any(data == 1))
ventes = np.random.randint(0, 200, 7)
print(ventes)
print(np.mean(np.diff(ventes)))
