###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - De salto em salto
# Nome: Jackeline Leme Gregório
# RA: 173678
###################################################


def propagação_de_fake_news(matriz, x, y):
    intensidade = int(matriz[x][y])
    matriz[x][y] = 'X'
    i = 1
    while i < intensidade + 1:
        if x+i < len(matriz):
            if matriz[x+i][y] == '#':
                break
            if matriz[x+i][y].isdigit():
                matriz = propagação_de_fake_news(matriz, x+i, y)
            i = i + 1
        else:
            break

    i = 1
    while i < intensidade + 1:
        if x-i >= 0:
            if matriz[x-i][y] == '#':
                break 
            if matriz[x-i][y].isdigit():
                matriz = propagação_de_fake_news(matriz, x-i, y)
            i = i + 1
        else:
            break

    i = 1
    while i < intensidade + 1:      
        if y+i < len(matriz[0]):
            if matriz[x][y+i] == '#':
                break
            if matriz[x][y+i].isdigit():
                matriz = propagação_de_fake_news(matriz, x, y+i)
            i = i + 1
        else:
            break
        
    i = 1
    while i < intensidade + 1:
        if y-i >= 0:
            if matriz[x][y-i] == '#':
                break 
            if matriz[x][y-i].isdigit():
                matriz = propagação_de_fake_news(matriz, x, y-i)
            i = i + 1
        else:
            break
                   
    return matriz



# Leitura de dados
n = int(input())
matriz = []
for _ in range(n):
    matriz.append(list(input()))
x, y = [int(i) for i in input().split()]

# Atualiza a matriz com a propagação da noticia falsa.
matriz = propagação_de_fake_news(matriz, x, y)

# Impressão do resultado
for line in matriz:
    print("".join(line))