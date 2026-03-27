import numpy as np
import leitura

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


def matriz_identidade(n):
    matriz_id = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if (i==j):
                matriz_id[i][j] = 1
    return matriz_id

# testes

A = np.array([
    [3,2,1],
    [1,1,1],
    [0,2,1]
])

A, b, c, sinais = leitura.ler_sistema("funcoes.txt")

print(inversa(A))
print("\n")
# multiplicação de matrizes: A @ A-¹ deve ser uma matriz identidade
print(A @ inversa(A))
print("\n")
print("custo = ", c)
print("\n")
print("matriz b = ", b)
print("\n")
print("sinais = ", sinais)

