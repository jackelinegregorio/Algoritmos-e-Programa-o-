w=[0, 1, 1, 1, 0, -1, -1, -1]
z=[1, 1, 0, -1, -1, -1, 0, 1]

def k(m, n, a, b):
  return 0<=a and a<m and 0<=b and b<n;

def word(matriz, linha, coluna, palavra, ind):
  
  if ind >= len(palavra):
    return 1
  
  sm=0
  
  for i in range(0,8):
    a=linha+w[i]
    b=coluna+z[i]
    if k(len(matriz), len(matriz[0]), a,b) and palavra[ind]==matriz[a][b]:
      sm = sm + word(matriz, a, b, palavra, ind+1)
  return sm

matriz=[]
n=0
while True:
  s=input()
  if s.isnumeric():
    n=int(s)
    break;
  matriz.append(s.split())
# Leitura das palavras
palavra= []

for i in range (0, n):
  s=input()
  palavra.append(s)
palavra.sort()

print(40*"-")
print("Lista de Palavras")
print(40*"-")

a=len(matriz)
b=len(matriz[0])

for i in range (0, len(palavra)):
  posicao=[]
  for j in range(0,a):
    for y in range(0,b):
      if matriz[j][y]==palavra[i][0]:
        num=word(matriz,j,y,palavra[i], 1)
        if num>0:
          posicao.append([j+1,y+1])
  print("Palavra:", palavra[i])
  print(("Posicoes: "+" ".join([str((a, b)) for a, b in posicao])).strip())
  print(40* "-")
