###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Caça-Números
# Nome: Jackeline Leme Gregório
# RA: 173678
###################################################
def verificador(caractere, valor):
    if valor == 1:
        if caractere == 'S' or caractere == 'A' or caractere == 'O':
            return True
    elif valor == 2:
        if caractere == 'P' or caractere == 'A' or caractere == 'E':
            return True
    elif valor == 3:
        if caractere == 'T' or caractere == 'A' or caractere == 'O' or caractere == 'P':
            return True
    elif valor == 4:
        if caractere == 'C' or caractere == 'A' or caractere == 'E':
            return True
    elif valor == 5:
        if caractere == 'P' or caractere == 'A' or caractere == 'O':
            return True
    elif valor == 6:
        if caractere == 'T' or caractere == 'A' or caractere == 'E' or caractere == 'C':
            return True
    elif valor == 7:
        if caractere == 'P' or caractere == 'A' or caractere == 'O':
            return True
    elif valor == 8:
        if caractere == 'C' or caractere == 'A' or caractere == 'E':
            return True
    elif valor == 9:
        if caractere == 'C' or caractere == 'A' or caractere == 'O' or caractere == 'T':
            return True
    return False

def busca_padrao(matriz, linha, coluna, padrao):
    rett = False
    if padrao == []:
        rett = True
    else:
        if verificador(padrao[0], matriz[linha][coluna]) == 1:
            if linha-1 >= 0:
                if busca_padrao(matriz, linha-1, coluna, padrao[1:]):
                   rett = True
            if linha+1 < len(matriz):
                if busca_padrao(matriz, linha+1, coluna, padrao[1:]):
                    rett = True
            if coluna+1 < len(matriz[0]):
                if busca_padrao(matriz, linha, coluna+1, padrao[1:]):
                    rett = True
            if coluna-1 >= 0 :
                if busca_padrao(matriz, linha, coluna-1, padrao[1:]):
                    rett = True
            if linha-1 >= 0 and coluna+1 < len(matriz[0]) :
                if busca_padrao(matriz, linha-1, coluna+1, padrao[1:]):
                    rett = True
            if linha+1 < len(matriz) and coluna-1 >= 0 :
                if busca_padrao(matriz, linha+1, coluna-1, padrao[1:]):
                    rett = True
            if linha+1 < len(matriz) and coluna+1 < len(matriz[0]) :
                if busca_padrao(matriz, linha+1, coluna+1, padrao[1:]):
                    rett = True
            if linha-1 > 0 and coluna-1 >= 0 :
                if busca_padrao(matriz, linha-1, coluna-1, padrao[1:]):
                    rett = True
    return rett 

# Leitura da matriz
matriz = []
line = input()
while line[0].isdigit():
    line = line.split()
    matriz.append([int(i) for i in line])
    line = input()
padrao = list(line)

# Processamento da busca na matriz

posicoes = []
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if busca_padrao(matriz, i, j, padrao):
            posicoes.append([i+1,j+1])

# Impressão das posições iniciais (linha e coluna)

if posicoes == []:
  print("Nenhum padrao encontrado!")
else:
  print(("Posicoes: " + " ".join([str((linha, coluna)) for linha, coluna in posicoes])).strip())