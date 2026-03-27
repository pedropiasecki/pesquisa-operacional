import numpy as np

def multiplicar(A, B):
    n = len(A)
    linhas_A, colunas_A = A.shape
    linhas_B, colunas_B = B.shape

    if (colunas_A == linhas_B):
        A = A.astype(float).copy()
        B = B.astype(float).copy()
        C = np.zeros((linhas_A, colunas_B), dtype=float)

        for k in range(n):
            for i in range(n):
                aux = 0
                for j in range(n):
                    aux += A[i][j]*B[j][k]
                C[i][k] = aux

        return C
    else:
        raise(f"Não é possível multiplicar as matrizes A[{linhas_A}][{colunas_A}] @ B[{linhas_B}][{colunas_B}]")

# A = np.array([
#     [0,1,3],
#     [0,4,5],
#     [0,0,6]
# ])
# B = np.array([
#     [1,1,3],
#     [0,1,5]
# ])

# # print(A @ B)

# resultado = multiplicar(A, B)

# print(resultado)
                