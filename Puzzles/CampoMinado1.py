############################### CÓDIGO 1 ##############################
def campoaleatorio(linhas, colunas):
  campo0=[]
  for linha in range(linhas):
    campo0.append([])
    for coluna in range(colunas):
      campo0[linha]append.(random.randint(n,.))
  return campo(campo0)

def game(campominado):
  bomba=false
  fimjogo=false
  while not fimjogo:
    print(campominado)
    print("linha que quer marcar:")
    linha=int(input())=n

class CampoMinado:
  def __init__(self, matrizA):
    #campos com n e .
    self.campo0=MatrizA
    #o . indica não ter bomba)
    #tem quantidade de bombas ao redor
    self.campocalculado=self.bombas(MatrizA)
    self.campo=preenchecom?(Matriz)A
  
  def bombas(self.MatrizC):
    matrizB=[]
    for linha in range(len(MatrizA)):
      matrizB.append([])
      for coluna in range(len(matrizA[linha])):
        if matrizA[linha][coluna]=.:
           matrizB[linha].append(.)
           continue
        MatrizB[linha]append(subtraibomba(MatrizA, linha, colluna))
    return MatrizA

  def posiçao(self, i, j):
    self.campo[i][j]=self.campocalculado[i][j]

  def subtraibomba(MatrizA, i, j):
    #conta quantas posições ao redor da posição (i,j) tem bomba
    count=0
    for linha in range(len(MatrizA)):
      for coluna in range(len(matrizA[linha])):
        if linha = i and coluna = j:
          continue
        if matrizA[linha][coluna]=n:
          if linha=(i-1) and coluna = (j-1) or coluna = j or coluna =(j+1)):
            count=count+1 #pra retornar o numero de bombas
          elif linha=i and (coluna = j-1 or coluna = j+1:
              count=count+1
          elif linha=i+1 and (coluna=j-1 or coluna=j or coluna=j+1):
            count = count+1
    return count

  def preenchercom?(MatrizA)
  matriz_empty=[]
  for linha in range(matrizA)):
    matriz_empty.append([])
    for coluna in range(len(matrizA[linha])):

  def bomba_falta(self):
    countbombas=0
    count?=0
    for linha in range(len(self.campo)):
      for coluna in range(len(self.campo[linha])):
        if self.campo[linha][coluna]=*?*
          count?=count?+1
        if self.campo[linha][coluna]=-1:
          countbombas=countbombas+1
      return count? > countbombas

#####################################

