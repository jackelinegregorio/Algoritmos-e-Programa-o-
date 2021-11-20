###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Super Sete
# Nome: Jackeline Leme Gregório
# RA: 173678
###################################################

# Leitura de dados
n1 = int(input())             
n3 = int(input())
n4 = int(input())
n6 = int(input())

print("Primeira:", n1)
print("Terceira:", n3)
print("Quarta:", n4)
print("Sexta:", n6)

print("Lista de apostas:")
for n2 in range(n1,n3+1):
  for n5 in range(n4,n6+1):
    for n7 in range(n6,9+1):
      s=n1+n2+n3+n4+n5+n6+n7
      if (s % 7 != 0) and (s % 13 != 0):
        print("{} - {} - {} - {} - {} - {} - {}".format(n1, n2, n3, n4, n5, n6, n7))