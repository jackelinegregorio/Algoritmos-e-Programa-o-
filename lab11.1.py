###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Jogo da Similaridade Máxima
# Nome: Jackeline Leme Gregório
# RA: 173678
###################################################

def calcula_similaridade(linha, coluna, maior, menor):
    similaridade = 0
    m = len(menor)

    i_ = 0
    for i in range(linha, linha + m):
        j_ = 0
        for j in range(coluna, coluna + m):
            if maior[i][j] == menor[i_][j_]:
                similaridade += 1
            j_ += 1
        i_ += 1
    return 100 * (similaridade / (len(menor)**2))

# Entradas
n = int(input())
maior = [[int(i) for i in input().split()] for _ in range(n)]

m = int(input())
menor = [[int(i) for i in input().split()] for _ in range(m)]

# Guardar
similaridade = [[0, 0, 0]]
for i in range(n - m + 1):
    for j in range(n - m + 1):
        similaridade.append([i, j, calcula_similaridade(i, j, maior, menor)])        

# Ordenar a matriz ordem decrescente de similaridade
similaridade = sorted(similaridade, key=lambda l: l[-1], reverse=True)

*pos, similaridade_maxima = similaridade[0]

print("Posição: ({0},{1})".format(pos[0], pos[1]))
print("Similaridade máxima: {:.2f}%".format(similaridade_maxima))
