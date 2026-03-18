import numpy as np
# ler arquivo Ax = b
# funcao -> 
# b ->
# c -> sinais {>, =, >=, <=}
# A -> matriz A
def ler_sistema(nome_arquivo):
    with open(nome_arquivo, "r") as f:
        linhas = f.readlines()

    # primeira linha
    funcao = list(map(float, linhas[0].split()))

    # b é a ultima linha
    b = list(map(float, linhas[-1].split()))

    # c é a penultima linha
    c = list(map(str, linhas[-2].split()))

    A = np.array([list(map(float, linha.split())) for linha in linhas[1:-2]])

    return A, b, c, funcao