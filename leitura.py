import numpy as np
import re

def ler_sistema(nome_arquivo):
    with open(nome_arquivo, "r") as f:
        linhas = [l.strip() for l in f.readlines() if l.strip()]

    ## numero de variaveis
    todas_vars = re.findall(r'x(\d+)', " ".join(linhas))
    n = max(map(int, todas_vars))

    ## cria o vetor de custo
    c = np.zeros(n)
    termos = re.findall(r'([+-]?\s*\d*)x(\d+)', linhas[0])

    # trata os sinais
    for coef, var in termos:
        coef = coef.replace(" ", "")
        if coef in ["", "+"]:
            coef = 1
        elif coef == "-":
            coef = -1
        else:
            coef = int(coef)

        c[int(var) - 1] += coef

    ## regras do sistema
    A = []
    b = []
    sinais = []

    # cada linha uma regra
    for linha in linhas[1:]:
        # identificar sinal da regra
        match = re.search(r'(<=|>=|=|<|>)', linha)
        sinal = match.group(0)

        # separa os lados A, b
        esquerda, direita = linha.split(sinal)

        linha_A = np.zeros(n)
        termos = re.findall(r'([+-]?\s*\d*)x(\d+)', esquerda)

        for coef, var in termos:
            coef = coef.replace(" ", "")
            if coef in ["", "+"]:
                coef = 1
            elif coef == "-":
                coef = -1
            else:
                coef = int(coef)

            linha_A[int(var) - 1] += coef

        A.append(linha_A)
        b.append(float(direita.strip()))
        sinais.append(sinal)

    return np.array(A), np.array(b), c, sinais

