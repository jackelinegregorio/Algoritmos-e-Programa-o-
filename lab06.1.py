###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Plataforma
# Nome: Jackeline Leme Gregório
# RA: 173678
###################################################

# Leitura de dados
plataforma = [int(i) for i in input().split()]
i = int(input())-1
visitados=[i]
while True:
  print(i+1)
  i=i+plataforma[i]
  if i<0:
    print("esquerda")
    break
  if i>=len(plataforma):
    print("direita")
    break
  if i in visitados:
    print("loop")
    break
  visitados.append(i)