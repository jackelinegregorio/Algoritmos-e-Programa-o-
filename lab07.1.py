###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - A Viagem
# Nome: Jackeline Leme Gregório
# RA: 173678
###################################################

# Leitura de dados
N = int(input())
W = int(input())


# Função que coloca N itens dados pelo usuário em uma lista.
def recebe_itens(n=N):
    arr = []

    for _ in range(n):
        var = int(input())
        arr.append(var)

    return arr


weights = recebe_itens()
values = recebe_itens()

# Criando uma tabela parecida com a do enunciado
table = sorted([[values[i], weights[i], values[i]/weights[i]] for i in range(N)], key=lambda item: (item[-1], item[0]), reverse=True)

# Escolha dos itens da mochila
knapsack_weight = 0
knapsack_value = 0

i = 0
while i < len(table):
    if table[i][1] + knapsack_weight <= W:
        knapsack_value += table[i][0]
        knapsack_weight += table[i][1]
    i += 1

print(knapsack_value)
print(knapsack_weight)

