###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Números da Mega-Sena
# Nome: Jackeline Leme Gregório
# RA: 173678
###################################################

# Leitura de dados

n1 = int(input())             
n3 = int(input())
n4 = int(input())
n6 = int(input())

print("Primeiro:", "{:02}".format(n1))
print("Terceiro:", "{:02}".format(n3))
print("Quarto:", "{:02}".format(n4))
print("Sexto:", "{:02}".format(n6))

print("Lista de apostas:")
for n2 in range(n1+1,n3,2):
  for n5 in range(n4+1,n6,2):
    a = n1 + n2 + n3 + n4 + n5 + n6
    if (a % 7 != 0) and (a % 13 != 0):
      print("{:02} - {:02} - {:02} - {:02} - {:02} - {:02}".format(n1, n2, n3, n4, n5, n6))

