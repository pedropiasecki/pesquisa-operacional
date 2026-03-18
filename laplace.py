import numpy as np
import leitura

# cria uma sub matriz usando os valores fora de i, j
# retorna a sub matriz criada
def sub_matriz(A, linha, coluna):
    n = len(A)
    sub = []

    for i in range(n):
        if i != linha:
            nova_linha = []
            for j in range(n):
                if j != coluna:
                    nova_linha.append(A[i][j])
            sub.append(nova_linha)

    return sub

# função recursiva do  laplace
def laplace(A):
    n = len(A)

    if (n==0):
        raise("Matriz vazia.")
    
    if (n==1):
        return A[0][0]
    if (n==2):
        return A[0][0] * A[1][1] + (-(A[0][1] * A[1][0]))
    
    det = 0
    for j in range(n):
        sub = sub_matriz(A, 0, j)
        det += (-1)**j * A[0][j] * laplace(sub)

    return det
    
    
# A = np.array([
#     [2,1,3],
#     [0,4,5],
#     [0,0,6]
# ])

# # A, b, c, funcao = leitura.ler_sistema("funcoes.txt")


# resultado = laplace(A)
# print(resultado)