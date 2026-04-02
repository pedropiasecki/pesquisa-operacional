import numpy as np
import leitura as lt

"""
Método da Inversa usando eliminação de Gauss
"""
def inversa(A):
    n = len(A)
    id = matriz_identidade(n)

    A = A.astype(float).copy()
    id = id.astype(float).copy()

    # linha do pivo
    for k in range(n):

        pivo = A[k][k]
        maior_valor = abs(pivo)
        linha_pivo = k

        # procura o maior valor
        for aux in range(k+1, n):
            if abs(A[aux][k]) > maior_valor:
                maior_valor = abs(A[aux][k])
                linha_pivo = aux
        
        # trocar linhas
        if k != linha_pivo:
            for aux in range(n):
                temp = A[linha_pivo][aux]
                temp2 = A[k][aux]
                A[k][aux] = temp
                A[linha_pivo][aux] = temp2
            
            tempB = id[linha_pivo].copy()
            id[linha_pivo] = id[k]
            id[k] = tempB

        if maior_valor == 0:
            raise ValueError("Pivo zero, matriz nao possui inversa")

        pivo = A[k][k]

        # normalizar linha do pivô
        for j in range(n):
            A[k][j] = A[k][j] / pivo
            id[k][j] = id[k][j] / pivo

        # zerar as outras linhas
        for i in range(n):
            if i != k:
                m = A[i][k]

                for j in range(n):
                    A[i][j] -= m*A[k][j]
                    id[i][j] -= m*id[k][j]

    return id


"""
Gera uma matriz identidade de tamanho n
"""
def matriz_identidade(n):
    matriz_id = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if (i==j):
                matriz_id[i][j] = 1
    return matriz_id


""" 
cria uma sub matriz usando os valores fora de i, j
retorna a sub matriz criada
"""
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


"""
Método laplace recursivo para calcular o determinante de uma matriz
"""
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


"""
Método de multiplicação de matrizes A@B
"""
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