

def recursao(i, j, valor_vertical, valor_horizontal, passou, matriz, retorno, linhas, colunas):
    if(j == valor_horizontal and i == valor_vertical):
        return 1

    if not([i,j] in passou) :
        

        #baixo
        if(i + matriz[i][j] < linhas and retorno != 1 and passou[i+matriz[i][j]][j] == 0):

            passou[i + matriz[i][j]][j] = 1
            retorno = recursao(i+matriz[i][j], j, valor_vertical, valor_horizontal, passou, matriz, retorno, linhas, colunas)
            passou[i + matriz[i][j]][j] = 0
        #cima
        if(i - matriz[i][j] >= 0 and retorno != 1 and passou[i-matriz[i][j]][j] == 0):

            passou[i - matriz[i][j]][j] = 1
            retorno = recursao(i-matriz[i][j], j, valor_vertical, valor_horizontal, passou, matriz, retorno, linhas, colunas)
            passou[i - matriz[i][j]][j] = 0
        #direita
        if(j + matriz[i][j] < colunas and retorno != 1 and passou[i][matriz[i][j]+j] == 0):

            passou[i][matriz[i][j]+j] = 1
            retorno = recursao(i, matriz[i][j]+j, valor_vertical, valor_horizontal, passou, matriz, retorno, linhas, colunas)
            passou[i][matriz[i][j]+j] = 0
        #esquerda
        if(j - matriz[i][j] >= 0 and retorno != 1 and passou[i][-matriz[i][j]+j] == 0):

            passou[i][-matriz[i][j]+j] = 1
            retorno = recursao(i,-matriz[i][j]+j, valor_vertical, valor_horizontal, passou, matriz, retorno, linhas, colunas)
            passou[i][-matriz[i][j]+j] = 0
        return retorno





a = input().split()
linhas = int(a[0])
colunas = int(a[1])
matriz = []
passou = []
for i in range(linhas):

    b = input().split()
    passou.append([0]*len(b))
    for j in range(len(b)):
        b[j] = int(b[j])
    matriz.append(b)


a = input().split()
comeco1 = int(a[0])
fim1 = int(a[1])
a = input().split()
comeco2 = int(a[0])
fim2 = int(a[1])
retorno = recursao(comeco1, fim1, comeco2,fim2, passou, matriz, 0, linhas, colunas)
caminho_1 = "existe caminho"
caminho_2 = "nao existe caminho"
if(retorno == 1):
    print("({},{}) -> ({},{}):".format(comeco1,fim1,comeco2,fim2), caminho_1)
else:
    print("({},{}) -> ({},{}):".format(comeco1,fim1,comeco2,fim2), caminho_2)

retorno = recursao(comeco2, fim2, comeco1,fim1, passou, matriz, 0, linhas, colunas)
if(retorno == 1):
    print("({},{}) -> ({},{}):".format(comeco2,fim2,comeco1,fim1), caminho_1)
else:
    print("({},{}) -> ({},{}):".format(comeco2,fim2,comeco1,fim1), caminho_2)
