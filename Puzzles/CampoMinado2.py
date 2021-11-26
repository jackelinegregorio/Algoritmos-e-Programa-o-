############################### CÓDIGO 2 ##############################
import random
import sys
import math

# . é nenhum perigo em qualquer lugar ao redor de 8 espaços
# n minas escondidas ao redor de 8
# ? não sabemos nada
#h=3 #altura é <=3
#C=20 #largura é <=20
#nb >= 1 and nb <=20 #minas escondidas 1<=nb<=20

grid = [[0,1,2,5,4,6,0,0,0,0],
        [0,1,2,5,4,6,0,0,0,0],
        [0,1,2,5,4,6,0,0,5,0],
        [0,1,2,5,4,6,0,0,0,0],
        [0,1,2,5,4,6,0,0,0,0],
        [0,1,2,5,4,6,6,0,0,0]]
        
#gerar bombas
#gerar bombas em locais aleatórios
def local_bombas(b):
  h = random.randint(0, 3)
  C = random.randint(0, 20)
  #Verifica se há uma bomba no local gerado aleatoriamente. Se não, ele coloca um lá. Se houver, ele solicita um novo local para tentar..
  linha = b[h]
  if not linha[C] == 'n':
      linha[C] = 'n'
  else:
    local_bombas(b)
      #reset()
for h in range (0, 3):
  for C in range (0, 20):
    valor = l(h, C, b)
    if value == 'n':
         atualizavalor(h, C, b)


for nb in range (1, 20):
  localbomba(b)
    #reset()

def atualizavalor(nm, C, b):
    if hn-1 > -1:
     h = b[nm-1]
    if C-1 > -1:
          if not h[C-1] == 'n':
                h[C-1] += 1

    if not r[c] == 'n':
            h[C] += 1
    if 9 > C+1:
          if not h[C+1] == 'n':
                h[C+1] += 1

#mesma linha  
    h = b[hm]
    if C-1 > -1:
        if not h[C-1] == 'n':
            h[C-1] += 1

    if 9 > c+1:
        if not h[C+1] == 'n':
            h[C+1] += 1

#abaixo
    if 9 > rn+1:
        r = b[rn+1]

        if c-1 > -1:
            if not r[c-1] == '*':
                r[c-1] += 1

        if not r[c] == '*':
            r[c] += 1

        if 9 > c+1:
            if not r[c+1] == '*':
                r[c+1] += 1
#o valor de uma coordenada no grid.
def l(r, c, b):
    row = b[r]
    c = row[c]
    return c
#o valor de uma coordenada no grid.
def l(r, c, b):
    c = b[r][c]
    return c
#o valor de uma coordenada no grid.
def l(r, c, b):
    return b[r][c]