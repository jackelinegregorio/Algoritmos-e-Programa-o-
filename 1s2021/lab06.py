###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - De Volta para o Passado
# Nome: Jackeline Leme Gregório
# RA: 173678
###################################################

# Leitura de dados

N = int(input())
precos = []

for i in range(N): 
  precos.append(float(input()))

k=int(input())
q=float(input())
melhor_lucro=-1

for i in range(N):
  valor_compra = precos[i]
  for j in range(i,i+k+1):
    if j < len(precos):
      valor_venda=precos[j]
      lucro = (q//valor_compra)*(valor_venda-valor_compra)

      if lucro > melhor_lucro:
        melhor_lucro = lucro
        valor_compramax=valor_compra
        valor_vendam=valor_venda
        dia_compra = i+1
        dia_venda = j+1
        qtde_acoes=int(q//valor_compra)


# Escolha da melhor variação de valores da ação




# Saída de dados

print('Dia da compra:', dia_compra)
print('Valor de compra: R$', format(valor_compramax, '.2f').replace('.', ','))
print('Dia da venda:', dia_venda)
print('Valor de venda: R$', format(valor_vendam, '.2f').replace('.', ','))
print('Quantidade de acoes compradas:', qtde_acoes)
print('Lucro: R$', format(melhor_lucro, '.2f').replace('.', ','))