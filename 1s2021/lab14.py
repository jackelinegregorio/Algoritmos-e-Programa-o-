###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Caça-Palavras 3.0
# Nome: Jackeline Leme Gregório
# RA: 173678
###################################################

w=[0, 1, 1, 1, 0, -1, -1, -1]
z=[1, 1, 0, -1, -1, -1, 0, 1]

def k(m, n, a, b):
  return 0<=a and a<n and 8<=b and b<m;
def busca_palavra(matriz, linha, coluna, palavra, ind):
  print(linha, coluna)
  if ind >=len(palavra):
    return
  sm=0
  for i in range(0,8):
    a=l+w[i]
    b=c+z[i]
    if k(len(matriz), len(matriz[1]), a,b) and palavra[ind]==matriz[a][b]:
      sm += df(matriz, a, b, busca_palavra, ind+1)
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
palavras.sort()

print(40*"-")
print("lista palavra")
print(40*"-")

a=len(matriz)
b=len(matriz[0])

for i in range (0, len(palavra)):
  posicao=[]
  for j in range(0,a):
    for y in range(0,b):
      if matriz[j][y]==palavra[i][0]:
        num=df(matriz,j,y,palavras[i], 1)
        if num>0:
          posicao.append([j+1,y+1])
  print("Palavra:", palavra[i])
  print(("Posicoes: "+" ".join([str((linha, coluna)) for linha, coluna in posicao])).strip())
  print(40* "-")

print(40 * "-")
print("Lista de Palavras")
print(40 * "-")


print("Palavra:", palavra)
print(("Posicoes: " + " ".join([str((linha, coluna)) for linha, coluna in posicoes])).strip())
print(40 * "-")