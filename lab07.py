###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Nota de MC102
# Nome: Jackeline Leme Gregório
# RA: 173678
###################################################


qnt_lab = int(input())

notas = []
peso = []

for i in range (qnt_lab):
  notas.append(float(input()))

for i in range(qnt_lab):
  peso.append(int(input()))

media_nota = 0

for i in range (qnt_lab):
  media_nota = media_nota + notas[i]*peso[i]
media_nota = media_nota/sum(peso)
print("Media laboratorios:", format(media_nota, ".1f").replace(".", ","))
if media_nota >= 5:
  nota_final = media_nota #media_ponderada
  print("Situacao: Aprovado por nota")
if media_nota <2.5:
  nota_final = media_nota #media_ponderada
  print("Situacao: Reprovado por nota")

if media_nota >=2.5 and media_nota <5:
  m = int(input())
  indices = []
  for i in range (m):
    p = int(input())-1
    indices.append(p)
  notas_exame = []
  for i in range (m):
    p = float(input())
    notas_exame.append(p)
  media_exame = 0
  pesos = 0
  for i in range (m):
    media_exame = media_exame + notas_exame[i]*peso[indices[i]]
    pesos = pesos + peso[indices[i]]
  media_exame = media_exame/pesos
  nota_final = min(5,(media_exame+media_nota)/2)
  if nota_final == 5:
    print("Situacao: Aprovado no exame")
  else:
    print("Situacao: Reprovado no exame")
print("Nota final:", format(nota_final, ".1f").replace(".", ","))

#nota final = mínimo{5, (média ponderada dos laboratórios + média ponderada do exame) / 2}#lista de labs pro exame