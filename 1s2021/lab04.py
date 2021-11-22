###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Magic: The Gathering
# Nome: Jackeline Leme Gregório 
# RA: 173678
###################################################

# Leitura do orçamento, do valor do booster e da quantidade de cartas desejadas

x = float(input()) #orçamento
b = float(input()) #preço_booster
d = int(input()) #quantidade cartas
quantidade_cartas=0
total_gasto=0
quantidade_boosters=0
total_restante=x
preto=3
verde=5

# Leitura da sequência de cartas
while total_restante>=b:
  c=int(input())
  total_gasto=total_gasto+b
  quantidade_boosters=quantidade_boosters+1
  total_restante=total_restante-b
  if c==preto or c==verde:
    quantidade_cartas=quantidade_cartas+1
  if quantidade_cartas==d:
    break

# Impressão das informações de saída

print("ORCAMENTO: {:.2f} REAIS".format(x))
print("VALOR DO BOOSTER: {:.2f} REAIS".format(b))
print("TOTAL GASTO: {:.2f} REAIS".format(total_gasto))
print("TOTAL RESTANTE: {:.2f} REAIS".format(total_restante))
print("QUANTIDADE DE BOOSTERS COMPRADOS: {}".format(quantidade_boosters))
print("QUANTIDADE DESEJADA DE CARTAS DA COR VERDE OU DA COR PRETA: {}".format(d))
print("QUANTIDADE OBTIDA DE CARTAS DA COR VERDE OU DA COR PRETA: {}".format(quantidade_cartas))

if quantidade_cartas==d:
  print("JOAO CONSEGUIU MONTAR SEU NOVO DECK!")
else:
  print("JOAO NAO CONSEGUIU MONTAR SEU NOVO DECK!")
