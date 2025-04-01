import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)
print(newarr)

#RESHAPE FROM 1D to 3D

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)

print(arr)

newarr = arr.reshape(2, 2, -1)
print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)
print(newarr)