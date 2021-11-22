###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Tabela de Vendas
# Nome: Jackeline Leme Gregório
# RA: 173678

# Leitura de dados
linhas = int(input()) 
tabela = [input().split(",")]
for line in range(linhas):
  raw = input().split(",")
  nao_raw = [int(x) for x in raw[1:]]
  tabela.append([raw[0]]+nao_raw)  

prioridade = input().split() 
def babysort(tabela,a):
  tam = len(tabela)-1
  sorted = False
  while not sorted:
    sorted = True
    for i in range(0, tam):
      if tabela[i][a]>tabela[i+1][a]:
        sorted = False
        tabela[i], tabela[i+1] = tabela[i+1], tabela[i]
  return tabela 

no_cabecalho = tabela[1:]  
for i in range(len(prioridade)):
  priodavez = prioridade[-1-i]
  index_a = tabela[0].index(priodavez)
  no_cabecalho=babysort(no_cabecalho,index_a)

tabela_f = [tabela[0]] + no_cabecalho
for linha in tabela_f: 
  print('{:15s}'.format(linha[0]), ''.join('{:>10}'.format(item) for item in linha[1:]))