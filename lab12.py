    ###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Filtros de Imagens
# Nome: Jackeline Leme Gregório
# RA: 173678


import copy
def imprime_imagem(imagem):
    print("P2")
    print(len(imagem[0]), len(imagem))
    print("255")
    for i in range(len(imagem)):
        print(" ".join(str(x) for x in imagem[i]))


def mediana(lista):
    lista_ordenada = sorted(lista)
    elemento_central = len(lista_ordenada) // 2
    if len(lista) % 2 == 1:
        return lista_ordenada[elemento_central]
    else:
        return (lista_ordenada[elemento_central - 1] + lista_ordenada[elemento_central]) // 2


def filtro_negativo(imagem):
    for m in range(len(imagem)):
        for n in range(len(imagem[0])):
            imagem[m][n] = 255 - imagem[m][n]


def filtro_mediana(imagem):
    imagem_copia = copy.deepcopy(imagem)
    for i in range(n):
        for j in range(m):
            l = []
            if i - 1 >= 0 and j - 1 >= 0:
                l.append(imagem[i - 1][j - 1])
            if i - 1 >= 0 and j + 1 < m:
                l.append(imagem[i - 1][j + 1])
            if j - 1 >= 0:
                l.append(imagem[i][j - 1])
            l.append(imagem[i][j])
            if i + 1 < n:
                l.append(imagem[i + 1][j])
            if j + 1 < m:
                l.append(imagem[i][j + 1])
            if i + 1 < n and j - 1 >= 0:
                l.append(imagem[i + 1][j - 1])
            if i - 1 >= 0:
                l.append(imagem[i - 1][j])
            if i + 1 < n and j + 1 < m:
                l.append(imagem[i + 1][j + 1])
            imagem_copia[i][j] = mediana(l)

    return imagem_copia


def convolucao(imagem, M, D):
    imagem_conv = []
    l = []
    for i in range(1, len(imagem) - 1):
        for j in range(1, len(imagem[0]) - 1):
            L1 = M[0][0] * imagem[i - 1][j - 1] + M[0][1] * imagem[i - 1][j] + M[0][2] * imagem[i - 1][j + 1]
            L2 = M[1][0] * imagem[i][j - 1] + M[1][1] * imagem[i][j] + M[1][2] * imagem[i][j + 1]
            L3 = M[2][0] * imagem[i + 1][j - 1] + M[2][1] * imagem[i + 1][j] + M[2][2] * imagem[i + 1][j + 1]
            pix = (L1 + L2 + L3) // D
            if pix < 0:
                pix = 0
            elif pix > 255:
                pix = 255
            l.append(pix)
        imagem_conv.append(l)
        l = []
    return imagem_conv

filtro = input()
_ = input()
m, n = [int(x) for x in input().split()]
print("M e N: ", m, n)
_ = input()
imagem = []
for i in range(n):
    linha = [int(x) for x in input().split()]
    imagem.append(linha)


if (filtro == "mediana"):
    imagem = filtro_mediana(imagem)
elif (filtro == "negativo"):
    filtro_negativo(imagem)
elif (filtro == 'edge-detect'):
    M = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
    D = 1
    imagem = convolucao(imagem, M, D) 
elif (filtro == 'sharpen'):
    M = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
    D = 1
    imagem = convolucao(imagem, M, D) 
elif (filtro == 'blur'):
    M = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    D = 9
    imagem = convolucao(imagem, M, D) 


imprime_imagem(imagem) 

