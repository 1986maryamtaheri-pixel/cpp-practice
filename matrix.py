import numpy as np

a = np.array([[1, 2], [3, 4]])
print("Matrix:")
print(a)
print("determinant =", round(np.linalg.det(a), 2))