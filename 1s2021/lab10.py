###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caça-Palavras 2.0
# Nome: Jackeline Leme Gregório
# RA: 173678
###################################################


def horizontal(palavra, matriz, linha, coluna, tamanho_palavra):
    ocorrencia = 0
    for i in range(linha):
        for j in range(coluna):
            if(matriz[i][j].lower() == palavra[0] or matriz[i][j] == '*'):
                k = 0
                while((k+j<coluna) and (k < tamanho_palavra) and ((matriz[i][j+k].lower() == palavra[k]) or (matriz[i][j+k] == '*'))):
                    k = k + 1
                if(k == tamanho_palavra):
                    ocorrencia = ocorrencia + 1
                    for n in range(tamanho_palavra):
                        if(matriz[i][j+n] != '*'):
                            matriz[i][j+n] = matriz[i][j+n].upper()
    return ocorrencia

def vertical(palavra, matriz, linha, coluna, tamanho_palavra):
    ocorrencia = 0
        for i in range(linha):
        for j in range(coluna):
            if(matriz[i][j].lower() == palavra[0] or matriz[i][j] == '*'):
                k = 0
                while((k+i<linha) and (k < tamanho_palavra) and ((matriz[i+k][j].lower() == palavra[k]) or (matriz[i+k][j] == '*'))):
                    k = k + 1
                if(k == tamanho_palavra):
                    ocorrencia = ocorrencia + 1
                    for n in range(tamanho_palavra):
                        if(matriz[i+n][j] != '*'):
                            matriz[i+n][j] = matriz[i+n][j].upper()
    return ocorrencia


def diagonal_sup(palavra, matriz, linha, coluna, tamanho_palavra):
    ocorrencia = 0
    for i in range(linha):
        for j in range(coluna):
            if(matriz[i][j].lower() == palavra[0] or matriz[i][j] == '*'):
                k = 0
                while((k+i<linha) and(k+j<coluna) and (k < tamanho_palavra) and ((matriz[i+k][j+k].lower() == palavra[k]) or (matriz[i+k][j+k] == '*'))):
                    k = k + 1
                if(k == tamanho_palavra):
                    ocorrencia = ocorrencia + 1
                    for n in range(tamanho_palavra):
                        if(matriz[i+n][j+n] != '*'):
                            matriz[i+n][j+n] = matriz[i+n][j+n].upper()
    return ocorrencia

def diagonal_inf(palavra, matriz, linha, coluna, tamanho_palavra):
    ocorrencia = 0
    for i in range(linha):
        for j in range(coluna):
            if(matriz[i][j].lower() == palavra[0] or matriz[i][j] == '*'):
                k = 0
                while((-k+i >= 0) and(k+j<coluna) and (k < tamanho_palavra) and ((matriz[i-k][j+k].lower() == palavra[k]) or (matriz[i-k][j+k] == '*'))):
                    k = k + 1
                if(k == tamanho_palavra):
                    ocorrencia = ocorrencia + 1
                    for n in range(tamanho_palavra):
                        if(matriz[i-n][j+n] != '*'):
                            matriz[i-n][j+n] = matriz[i-n][j+n].upper()
    return ocorrencia

matriz = []
lista = input().split()
while(not(lista[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9'])):
    matriz.append(lista.copy())
    lista = input().split()
i = 0
ocorrencia = 0
print("----------------------------------------\nLista de Palavras\n----------------------------------------")
while(i<int(lista[0])):
    lista2 = input()
    print("Palavra:",lista2)
    ocorrencia = horizontal(lista2, matriz, len(matriz), len(matriz[i]), len(lista2)) + ocorrencia
    ocorrencia = vertical(lista2, matriz, len(matriz), len(matriz[i]), len(lista2)) + ocorrencia
    ocorrencia = diagonal_inf(lista2, matriz, len(matriz), len(matriz[i]), len(lista2)) + ocorrencia
    ocorrencia = diagonal_sup(lista2, matriz, len(matriz), len(matriz[i]), len(lista2)) + ocorrencia
    print("Ocorrencias:",ocorrencia)
    print("----------------------------------------")
    ocorrencia = 0
    i = i + 1
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end="")
        if ( j!= len(matriz[0]) -1):
                print(" ",end="")
    print()