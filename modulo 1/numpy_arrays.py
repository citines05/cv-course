import numpy as np

# VETORES
# u = np.array([1, 3])
# v = np.array([3, 1])

# # soma e subtração de vetores
# print(u + v)
# print(u - v)

# # divisão e multiplicação de vetores
# print(u * v)
# print(u / v)
# print( 2 * u)

# # produto dot e produto vetorial
# print(np.dot(u, v))
# u1 = np.array([1, 3, 1])
# v1 = np.array([3, 1, 1])
# print(np.cross(u1, v1))

# MATRIZES
I = np.array([[1, 0], [0, 1]])
A = np.array([[2, 1], [1, 2]])

# soma e subtração de matrizes
print(I + A)
print(A - I)

# multiplicação de matrizes
print(np.matmul(A, I))