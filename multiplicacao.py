import numpy as np
import leitura

def multiplicar(A, B):
    n = len(A)

    A = A.astype(float).copy()
    B = B.astype(float).copy()
    C = np.zeros((3, 3), dtype=float)

    for k in range(n):
        for i in range(n):
            aux = 0
            for j in range(n):
                aux += A[i][j]*B[j][k]
            C[i][k] = aux
    
    return C

# A = np.array([
#     [2,1,3],
#     [0,4,5],
#     [0,0,6]
# ])
# B = np.array([
#     [1,1,3],
#     [0,1,5],
#     [0,1,6]
# ])

# print(A @ B)

# resultado = multiplicar(A, B)

# print(resultado)
                