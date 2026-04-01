import numpy as np
import re

# * se nao aparecer x1 entao é 0x1
# * salvar os indices x1...xn

def ler_sistema(nome_arquivo):
    with open(nome_arquivo, "r") as f:
        linhas = [l.strip() for l in f.readlines() if l.strip()]

    min_or_max = 0

    """
    ### Verificar se é min ou max
    1 - min
    0 - max
    """
    if re.search(rf"\b{re.escape('min')}\b", linhas[0]):
        min_or_max = 1 
    else:
        min_or_max = 0
        
    """
    ### Encontrar número de váriaveis
    (\\d+) serve para pegar 1 ou mais digitos apos a variavel x em todas as linhas
    """
    todas_vars = re.findall(r'x(\d+)', " ".join(linhas))
    n = max(map(int, todas_vars))

    """
    ### cria o vetor de custo
    [+-]? -> opcionalmente um sinal + ou -.
    \\s* -> zero ou mais espaços em branco.
    \\d* -> coeficiente -> zero ou mais dígitos.
    x -> x que separa os grupos
    () -> serve para criar grupos
    """
    c = np.zeros(n)
    termos = re.findall(r'([+-]?\s*\d*)x(\d+)', linhas[0])

    """
    ### trata os sinais
    if -> pega valores positivos do começo até o final, onde coeficiente é 1
    elif -> pega valores negativos do começo até o final, onde coeficiente é 1
    else -> | coeficientes |> 1, positivos ou negativos
    """
    for coef, var in termos:
        coef = coef.replace(" ", "")
        if coef in ["", "+"]:
            coef = 1
        elif coef == "-":
            coef = -1
        else:
            coef = int(coef)

        c[int(var) - 1] += coef

    """
    ### Leitura das regras do sistema
    separa cada linha em esquerda e direita a partir do sinal. O lado esquerdo é tratado da mesma forma
    que o vetor de custos, enquanto o lado direito é tratado diretamente
    A -> lado esquerdo forma uma matriz nxn
    b -> lado direito forma um vetor n
    sinais -> vetor que guarda o sinal de cada linha
    """
    A = []
    b = []
    sinais = []

    for linha in linhas[1:]:
        """
        .group(0) retorna o texto que eu match
        """
        match = re.search(r'(<=|>=|=|<|>)', linha)
        sinal = match.group(0)

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

    return normalizar(np.array(A), np.array(b), sinais, min_or_max)


def normalizar(A, b, sinais, min_or_max):
    n_linhas, n_colunas = A.shape

    A_normalizada = np.zeros((n_linhas, n_colunas+1))
    b_normalizado = np.zeros(n_linhas)

    for i in range(n_linhas):
        for j in range(n_colunas):
            A_normalizada[i][j] = A[i][j]
        
        if (sinais[i] in ['>', '>=']):
            A_normalizada[i][j+1] = -1
        else: A_normalizada[i][j+1] = 1

    A_normalizada = np.array(A_normalizada)
    
    if (min_or_max == 0):
        for i in range(n_linhas):
            for j in range(n_colunas+1):
                A_normalizada[i][j] *= -1
                
            b_normalizado[i] = b[i]*(-1)

    return A_normalizada, b_normalizado


ler_sistema('funcoes.txt')