#Faço dois vetores que me permitem andar em X e Y
#tem oito vetores
#o d1,d2 é o que somamos em i,j
dx = [ -1, -1, -1,  0, 0,  1, 1, 1 ]
dy = [ -1,  0,  1, -1, 1, -1, 0, 1 ]

#Pega a linha do input, dá um split e transforma numa lista com dois inteiros
h, w = [int(i) for i in input().split()]
minas_total = int(input())
grid = [list(input()) for _ in range(h)]
interrogação_total = 0
minas_encontrada = 0


def valid(x,y):
    return x >= 0 and x < h and y >= 0 and y < w

for i in range(h):
    for j in range(w):
        if grid[i][j] == '?':
            interrogação_total += 1

while minas_encontrada < minas_total: # Fica repetindo ate acabar
    if interrogação_total + minas_encontrada == minas_total: # Se a soma das interrogacoes + minas ja encontradas é igual ao total de bombas, marcamos com ?
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '?':
                    grid[i][j] = '#'
        minas_encontrada = minas_total
        interrogação_total = 0
    
    if minas_encontrada == minas_total: # Se ja encontrei todas, posso parar
        break

    for i in range(h):
        for j in range(w):
            if grid[i][j].isnumeric() is False or int(grid[i][j]) < 1 or int(grid[i][j]) > 8: # Se eu nao to numa casa de numero, posso seguir adiante, nao tem informacao aqui
                continue
            bomba_perto = 0  #Quantas bombas tenho em volta
            qmarks_near = 0 # Quantas "?"" tenho em volta
            for d1,d2 in zip(dx,dy): #zip para juntar as duas listas
                x = i + d1
                y = j + d2
                if valid(x,y):
                    if grid[x][y] == '?':
                        qmarks_near += 1
                    elif grid[x][y] == '#':
                        bomba_perto += 1

            if bomba_perto == int(grid[i][j]): # Se esse quadrado ja tem todas as bombas vizinhas
                for d1,d2 in zip(dx,dy):
                    x = i + d1
                    y = j + d2
                    if valid(x,y) and grid[x][y] == '?': 
                        grid[x][y] = '.' # Limpa todas as interrogacoes em volta
                        interrogação_total -= 1

            elif bomba_perto + interrogação_total == int(grid[i][j]): # Se esse quadrado nao tem todas as bombas vizinhas, mas as interrogacoes vizinhas preenchem
                for d1,d2 in zip(dx,dy):
                    x = i + d1
                    y = j + d2
                    if valid(x,y) and grid[x][y] == '?': # Marca as interrogacoes em volta
                        grid[x][y] = '#'
                        interrogação_total -= 1
                        minas_encontrada += 1  
ans = []
for i in range(h):
    for j in range(w):
        if grid[i][j] == '#':
            ans.append((j,i))
ans = sorted(ans)
for (i,j) in ans:
    print(i,j)

