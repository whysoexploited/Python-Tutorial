import numpy as np

matrix1 = np.array([[1, 3, 5],
                    [7, 9, 2],
                    [4, 6, 8]])

print(f"The 2x2 matrix is:{matrix1}")

matrix2 = np.array([[2, 3, 5],
                   [7, 14, 21],
                   [1, 3, 5]])

print(f"The 3x3 matrix:\n", matrix2)

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

#print("Matrix A:\n", A)
#print("Matrix B:\n", B)

# Matrix Multiplication

matrixmul = np.dot(A, B)

print("A x B: \n", matrixmul)

transposeA = np.transpose(A)
transposeB = np.transpose(B)

print(f"Transpose of A:\n{transposeA}")
print(f"Transpose of B:\n{transposeB}")

inversem1 = np.linalg.inv(matrix1)
inversem2 = np.linalg.inv(matrix2)

print("Inverse of matrix1: ", inversem1)
print("Inverse of matrix2: ", inversem2)

determinantm1 = np.linalg.det(matrix1)
determinantm2 = np.linalg.det(matrix2)

print("Determinant of matrix1:\n", determinantm1)
print("Determinant of matrix2:\n", determinantm2)

matrixf = np.array([[1, 2, 3],
                   [4, 5, 6]])

print("2x3 matrix is:\n", matrixf)

flattened = matrixf.flatten()
print(f'Flattened matrix= {flattened}')



