def flip_horizontal(imagem_original):
    m = len(imagem_original[0])
    nova_imagem = [[imagem_original[x][m - 1 - y] for y in range(m)] for x in range(len(imagem_original))]

    return nova_imagem

def flip_vertical(imagem_original):
    n = len(imagem_original)
    nova_imagem = [[imagem_original[n - 1 - x][y] for y in range(len(imagem_original[0]))] for x in range(n)]
    
    return nova_imagem

def shift_vertical(imagem_original, x):
    resto = [[imagem_original[i][j] for j in range(len(imagem_original[0]))] for i in range(len(imagem_original)-x)]
    imagem_nova = [[imagem_original[i][j] for j in range(len(imagem_original[0]))] for i in range(len(imagem_original)-x, len(imagem_original))]
    
    for line in resto:
        imagem_nova.append(line)

    return imagem_nova

def shift_horizontal(imagem_original, x):
    resto = [[imagem_original[i][j] for j in range(len(imagem_original[0])-x)] for i in range(len(imagem_original))]
    imagem_nova = [[imagem_original[i][j] for j in range(len(imagem_original[0])-x, len(imagem_original[0]))] for i in range(len(imagem_original))]
    i = 0
    for line in resto:    
        imagem_nova[i] += line
        i += 1

    return imagem_nova

def crop(imagem_original, x1, y1, x2, y2):
    return [[imagem_original[x][y] for y in range(y1-1, y2)] for x in range(x1-1, x2)]

def shrink(imagem_original):
    nova_imagem = []

    for x in range(len(imagem_original)//2):
        linha_nova_imagem = []
        for y in range(len(imagem_original[0])//2):
            novo_pixel = [[imagem_original[i][j] for j in range(y*2, y*2+2)] for i in range(x*2, x*2+2)]

            max_pixel = max([max(l) for l in novo_pixel])
            linha_nova_imagem.append(max_pixel)
        nova_imagem.append(linha_nova_imagem)
    
    return nova_imagem

# Recebendo as entradas
P2 = input()
m, n = map(int, input().split())
MAX_PIXEL = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
funcao = input()

matriz_resultado = []

# Recebo as entradas de cada função
if funcao == 'flip':
    orientacao = input()
    if orientacao == 'horizontal':
        matriz_resultado = flip_horizontal(p)
    else:
        matriz_resultado = flip_vertical(p)
elif funcao == 'shift':
    orientacao = input()
    x = int(input())
    if orientacao == 'horizontal':
        matriz_resultado = shift_horizontal(p, x)
    else:
        matriz_resultado = shift_vertical(p, x)
elif funcao == 'crop':
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    matriz_resultado = crop(p, x1, y1, x2, y2)
elif funcao == 'shrink':
    matriz_resultado = shrink(p)

# Mostro o resultado
print(P2)
print(len(matriz_resultado[0]), len(matriz_resultado))
print(MAX_PIXEL)
for linha in matriz_resultado:
    print(*linha)