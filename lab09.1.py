#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Magic: Trocando Cartas
# Nome: Jackeline Leme Gregório
# RA: 173678
#####################################################

cartas_para_troca = {}
cartas_desejadas = {}

# Leitura das cartas para troca
R=int(input())
k=0
while k<R:
  linha=input()
  id=linha.split(" ")[0]
  qnt=linha.split(" ")[1]
  cartas_para_troca[id]=qnt
  k+=1

# Leitura das cartas desejadas
D=int(input())
k=0
while k<D:
  linha=input()
  id=linha.split(" ")[0]
  qnt=linha.split(" ")[1]
  cartas_desejadas[id]=qnt
  k+=1

# Processamento das trocas
a=""
while a !="---":
  a=input()
  if a !="---":
    receber=a.split(" ")[0]
    dar=a.split(" ")[1]
    x = lambda carta: carta in cartas_desejadas.keys()
    y = lambda carta: carta in cartas_para_troca.keys()
    if y(dar) and not x(dar) and int(cartas_para_troca[dar])>0 or x(dar) and y(dar) and (cartas_para_troca[dar])>int(cartas_desejadas[dar]):
      print("TROCA REALIZADA!")
      cartas_para_troca[dar]=int(cartas_para_troca[dar])-1
      if receber in cartas_para_troca.keys():
        cartas_para_troca[receber]=int(cartas_para_troca[receber])+1
      else:
        cartas_para_troca[receber]=1
    else:
      print("TROCA NAO REALIZADA!")

# Processamento se as cartas desejadas foram obtidas
for cartas in cartas_desejadas.keys():
  if cartas in cartas_para_troca.keys() and int(cartas_desejadas[cartas])>int(cartas_para_troca[cartas]) or cartas not in cartas_para_troca.keys():
    print("JOAO NAO CONSEGUIU AS CARTAS DESEJADAS!")
    break
else:
  print("JOAO CONSEGUIU AS CARTAS DESEJADAS!")